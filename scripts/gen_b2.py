#!/usr/bin/env python3
"""Generate the four B2 vocabulary sections from the hand-written sources in scripts/b2_src/.

  dec_src.txt          -> dec.json  + dec_rules.json     (English -> German sound-shift decoder)
  fuz.txt + fuz_groups -> fuz.json  + fuz_groups.json    (collocation bug hunt)
  lazy.txt + ladders   -> lazy.json + lazy_ladders.json  (lazy word -> precise word)
  kon.txt              -> kon.json  + kon_table.json     (connector logic)

Usage:  python3 scripts/gen_b2.py
"""
import json
import os
import random
import re
import sys
import zlib
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "b2_src")
OUT = os.path.join(HERE, "..", "src", "data")


def lines(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as fh:
        for raw in fh:
            raw = raw.strip()
            if raw and not raw.startswith("#"):
                yield [f.strip() for f in raw.split("|")]


def dump(name, data):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def finish(ex, prefix, seed):
    """Order by level (A, B, C), shuffled inside a level, and number the exercises."""
    rng = random.Random(seed)
    ex.sort(key=lambda x: x["level"])
    for lv in "ABC":
        idx = [i for i, x in enumerate(ex) if x["level"] == lv]
        part = [ex[i] for i in idx]
        rng.shuffle(part)
        for i, p in zip(idx, part):
            ex[i] = p
    for i, x in enumerate(ex, 1):
        x["id"] = f"{prefix}-{i:04d}"
    return ex


def chain(steps, last):
    return "\n".join([f"{i}. {s}" for i, s in enumerate(steps, 1)] + [last])


# ===================================================================== DECODER
# id: (group, label, note, allowed correct segments, wrong segments)
RULES = {
    "P": ("Consonant shifts", "p → pf / f / ff", "Sound shift: English p became pf, f or ff in German",
          {"pf", "f", "ff"}, ["p", "pp", "ph", "b"]),
    "T": ("Consonant shifts", "t → z / ss / ß / tz", "Sound shift: English t became z, ss, ß or tz in German",
          {"z", "ss", "ß", "tz"}, ["t", "tt", "d", "ts", "th"]),
    "K": ("Consonant shifts", "k → ch", "Sound shift: English k (ck) became ch in German",
          {"ch"}, ["k", "ck", "g", "kh", "c"]),
    "D": ("Consonant shifts", "d → t", "Sound shift: English d became t in German",
          {"t"}, ["d", "dt", "tt", "th", "dh"]),
    "TH": ("Consonant shifts", "th → d", "Sound shift: English th became d in German",
           {"d"}, ["th", "t", "z", "dh", "s"]),
    "V": ("Consonant shifts", "v → b", "English v corresponds to German b (inside or at the end of a word)",
          {"b"}, ["v", "w", "f", "u"]),
    "ITY": ("Latin endings", "-ity → -ität", "Latin ending: -ity usually becomes -ität in German (feminine, die)",
            {"ität"}, ["ity", "itet", "ietät"]),
    "ISIEREN": ("Latin endings", "-ize → -isieren", "Latin ending: verbs in -ize / -ise usually end in -isieren in German",
                {"isieren"}, ["ieren", "izieren", "esieren"]),
    "ATE": ("Latin endings", "-ate → -ieren", "Latin ending: verbs in -ate usually end in -ieren in German",
            {"ieren"}, ["ate", "aten", "eren"]),
    "OUS": ("Latin endings", "-ous → -ös", "Latin ending: adjectives in -ous usually end in -ös in German",
            {"ös"}, ["ous", "os", "us"]),
    "IC": ("Latin endings", "-ic(al) → -isch", "Latin ending: adjectives in -ic / -ical usually end in -isch in German",
           {"isch"}, ["ic", "ich", "iesch", "isk"]),
    "IVE": ("Latin endings", "-ive → -iv", "Latin ending: adjectives in -ive usually end in -iv in German (no e)",
            {"iv"}, ["ive", "if", "ief"]),
    "ISM": ("Latin endings", "-ism → -ismus", "Latin ending: -ism is -ismus in German (masculine, der)",
            {"ismus"}, ["ism", "isum", "ismos"]),
    "URE": ("Latin endings", "-ure → -ur", "Latin ending: -ure loses its e and becomes -ur (feminine, die)",
            {"ur"}, ["ure", "ür", "our"]),
    "ENCE": ("Latin endings", "-ence/-ency → -enz", "Latin ending: -ence / -ency become -enz (feminine, die)",
             {"enz"}, ["ence", "ens", "enc"]),
    "ANZ": ("Latin endings", "-ance → -anz", "Latin ending: -ance becomes -anz (feminine, die)",
            {"anz"}, ["ance", "ans", "anc"]),
    "ARY": ("Latin endings", "-ary → -är", "Latin ending: -ary becomes -är in German",
            {"är"}, ["ary", "ar", "er"]),
    "C": ("Spelling", "c → k / z", "Spelling: German writes k before a, o, u and before consonants (class → Klasse), z before e, i, y",
          {"k", "z"}, ["c", "ck", "s", "ts", "kh"]),
    "PH": ("Spelling", "ph → f", "Spelling: modern German writes f where English has ph",
           {"f"}, ["ff", "v", "p", "pf"]),
}
RULE_LEVEL = {"Latin endings": "A", "Spelling": "A", "Consonant shifts": "B"}
DOUBLES_NOT_AT_START = {"ff", "pp", "tt", "ss", "ß", "tz", "dt", "ck", "kh"}
SEG = re.compile(r"\[([^\]]+)\]")


DROP_ENGLISH = {"ordinary", "ambulance", "residence", "ignorance", "pompous", "operate", "signature", "ominous",
                "dance", "reek", "separate", "magic", "military", "center", "kitchen"}  # false friends / loose matches
BAN_OPTIONS = {"Präsens", "Essens", "harmonieren", "Kelle", "Celle", "sanken", "zanken", "Woge", "oben", "Hertz",
               "Regen", "Bund", "Fund", "Bad", "Zorn", "Bug", "Buck", "süss", "dun", "Bus", "Dank", "Kunde"}  # real words


def build_dec():
    ex, examples, used = [], defaultdict(list), set()
    for f in lines("dec_src.txt"):
        assert len(f) == 5, f
        english, de_marked, rule, article, gloss = f
        if english.lower() in DROP_ENGLISH:
            continue
        assert rule in RULES, f
        m = SEG.findall(de_marked)
        assert len(m) == 1, f"one bracket pair needed: {f}"
        seg = m[0]
        group, label, note, allowed, wrong = RULES[rule]
        assert seg.lower() in allowed, f"segment {seg!r} not allowed for {rule}: {f}"
        word = SEG.sub(lambda x: x.group(1), de_marked)
        assert english.lower() not in used and word.lower() not in used, f"duplicate: {f}"
        used.update({english.lower(), word.lower()})
        start = SEG.search(de_marked).start() == 0
        cap = seg[0].isupper()
        pool = [p for p in sorted(allowed | set(wrong)) if p != seg.lower()]
        if start:
            pool = [p for p in pool if p not in DOUBLES_NOT_AT_START]
        pool = [p.capitalize() if cap else p for p in pool]
        rng = random.Random(zlib.crc32(english.encode()))
        alts = rng.sample(pool, len(pool))
        options = {word}
        for a in alts:
            cand = de_marked.replace(f"[{seg}]", a)
            if cand in BAN_OPTIONS or cand == word or len(options) >= 5:
                continue
            options.add(cand)
        options = sorted(options, key=lambda w: w.lower().replace("ä", "a").replace("ö", "o").replace("ü", "u"))
        assert word in options and len(options) >= 3, f
        shown = f"{article} {word}" if article != "-" else word
        steps = [
            f"English word: {english}" + (f"  (German meaning: {gloss})" if gloss.lower() != english.lower() else ""),
            f"Rule: {label} — {note}",
            f"Apply it: {english} → {de_marked}   (the bracket marks the changed part)",
        ]
        if article != "-":
            steps.append(f"Article: {article} (nouns keep their gender: {shown})")
        ex.append({
            "id": "", "level": RULE_LEVEL[group], "type": "cognate",
            "sentence": f"English: {english}  →  German: ___",
            "options": options, "answer": word, "case": group, "focus": label,
            "explanation": chain(steps, f"∴ {word}"),
            "tags": ["cognate", rule.lower(), group.lower()],
            "ref": {"table": "rules", "row": group, "col": rule},
        })
        if len(examples[rule]) < 3:
            examples[rule].append(f"{english} → {word}")
    groups = []
    for g in ["Consonant shifts", "Latin endings", "Spelling"]:
        items = [{"key": r, "label": RULES[r][1], "gloss": "e.g. " + " · ".join(examples[r])}
                 for r in RULES if RULES[r][0] == g and examples[r]]
        groups.append({"key": g, "title": g, "items": items})
    dump("dec.json", finish(ex, "D", 31))
    dump("dec_rules.json", groups)
    return len(ex), Counter(x["tags"][1] for x in ex)


# ===================================================================== BUG HUNT
def clean(tok):
    return re.sub(r"^[„“\"(]+|[.,;:!?“\")]+$", "", tok)


def build_fuz():
    groups = {}
    for f in lines("fuz_groups.txt"):
        anchor, rest = f[0], "|".join(f[1:])
        items = []
        for part in rest.split(";"):
            m = re.match(r"\s*(.+?)\s*\((.+)\)\s*$", part)
            assert m, f"bad partner: {part!r} in {f}"
            items.append({"key": m.group(1), "label": m.group(1), "gloss": m.group(2)})
        groups[anchor] = items
    ex, seen = [], set()
    for f in lines("fuz.txt"):
        assert len(f) == 7, f
        sentence, buggy, fixed, anchor, lemma, note, cands = f
        cands = [c.strip() for c in cands.split(",")]
        tokens = [clean(t) for t in sentence.split()]
        assert sentence not in seen, sentence
        seen.add(sentence)
        assert buggy in tokens and buggy in cands, f
        assert all(c in tokens for c in cands) and 4 <= len(cands) <= 6, f
        assert anchor in groups, f"unknown anchor {anchor}: {f}"
        assert lemma in [i["key"] for i in groups[anchor]], f"{lemma} not a partner of {anchor}: {f}"
        words = sentence.split(" ")
        pos = next(i for i, t in enumerate(words) if clean(t) == buggy)
        words[pos] = words[pos].replace(buggy, fixed, 1)
        corrected = " ".join(words)
        # candidates in sentence order
        options = sorted(set(cands), key=lambda c: tokens.index(c))
        partners = " · ".join(i["key"] for i in groups[anchor])
        steps = [
            f"Anchor: “{anchor}” fixes which partner is natural",
            f"Natural partners of {anchor}: {partners}",
            f"In the sentence “{buggy}” does not belong: {note}",
            f"Fix: {buggy} → {fixed}   (lemma: {lemma})",
        ]
        ex.append({
            "id": "", "level": "B", "type": "collocation_bug", "sentence": sentence,
            "options": options, "answer": buggy, "case": "Kollokation", "focus": f"{anchor} + {lemma}",
            "explanation": chain(steps, f"∴ {corrected}"),
            "tags": ["collocation", anchor.lower(), lemma],
            "ref": {"table": "ladder", "row": anchor, "col": lemma},
        })
    panel = [{"key": a, "title": a, "items": it} for a, it in sorted(groups.items())]
    dump("fuz.json", finish(ex, "F", 41))
    dump("fuz_groups.json", panel)
    return len(ex), Counter(x["tags"][1] for x in ex).most_common(3)


# ===================================================================== UPGRADE
def build_lazy():
    ladders = {}
    for f in lines("lazy_ladders.txt"):
        lazy, rest = f[0], "|".join(f[1:])
        items = []
        for part in rest.split(";"):
            word, _, gloss = part.partition("=")
            items.append({"key": word.strip(), "label": word.strip(), "gloss": gloss.strip()})
        ladders[lazy] = items
    ex, seen = [], set()
    for f in lines("lazy.txt"):
        assert len(f) == 7, f
        lazy, sentence, options, answer, lemma, need, compare = f
        options = [o.strip() for o in options.split(",")]
        assert lazy in ladders and sentence.count("___") == 1 and 3 <= len(options) <= 5, f
        assert answer in options and sentence not in seen, f
        seen.add(sentence)
        gloss = {i["key"]: i["gloss"] for i in ladders[lazy]}
        assert lemma in gloss, f"{lemma} not in ladder {lazy}: {f}"
        steps = [
            f"Lazy word: “{lazy}” is correct but says nothing about HOW / WHAT KIND",
            f"The sentence needs: {need}",
            f"Ladder: {lemma} = {gloss[lemma]}",
            f"The others: {compare}",
        ]
        ex.append({
            "id": "", "level": "B", "type": "lazy_upgrade",
            "sentence": f"Instead of „{lazy}“:  {sentence}",
            "options": sorted(options, key=str.lower), "answer": answer, "case": "Wortwahl", "focus": f"{lazy} → {lemma}",
            "explanation": chain(steps, f"∴ {answer}"),
            "tags": ["upgrade", lazy.lower(), lemma],
            "ref": {"table": "ladder", "row": lazy, "col": lemma},
        })
    panel = [{"key": k, "title": f"{k} →", "items": v} for k, v in ladders.items()]
    dump("lazy.json", finish(ex, "L", 51))
    dump("lazy_ladders.json", panel)
    return len(ex), Counter(x["tags"][1] for x in ex)


# ===================================================================== CONNECTORS
CLASSES = ["KONJ", "ADV", "NS"]
TABLE = [
    ("Grund", "cause", {"KONJ": ["denn"], "ADV": [], "NS": ["weil", "da"]}),
    ("Folge", "consequence", {"KONJ": [], "ADV": ["deshalb", "deswegen", "darum", "daher", "folglich", "somit", "infolgedessen"], "NS": ["sodass"]}),
    ("Gegensatz", "contrast", {"KONJ": ["aber", "sondern"], "ADV": ["allerdings", "hingegen", "dagegen", "jedoch"], "NS": ["während", "wohingegen"]}),
    ("Einräumung", "concession", {"KONJ": [], "ADV": ["trotzdem", "dennoch", "nichtsdestotrotz"], "NS": ["obwohl", "obgleich"]}),
    ("Bedingung", "condition", {"KONJ": [], "ADV": ["sonst", "andernfalls"], "NS": ["wenn", "falls", "sofern"]}),
    ("Zweck", "purpose", {"KONJ": [], "ADV": [], "NS": ["damit"]}),
    ("Zeit", "time", {"KONJ": [], "ADV": ["danach", "anschließend", "zuvor", "inzwischen"], "NS": ["bevor", "nachdem", "sobald", "bis", "seitdem"]}),
    ("Zusatz", "addition", {"KONJ": ["und"], "ADV": ["außerdem", "zudem", "überdies"], "NS": []}),
]
ORDER_TEXT = {
    "KONJ": "the subject follows right after the blank → coordinating conjunction (position 0, verb order unchanged)",
    "ADV": "the finite verb follows right after the blank → connecting adverb (position 1, verb in 2nd place)",
    "NS": "the verb sits at the END of the clause → subordinating conjunction",
}
CLASS_TITLE = {"KONJ": "Konj. (Pos 0)", "ADV": "Adverb (Pos 1)", "NS": "Nebensatz (Verb Ende)"}


def build_kon():
    cell = {(r, c): words for r, _, cols in TABLE for c, words in cols.items()}
    eng = {r: e for r, e, _ in TABLE}
    word_to = {w.lower(): (r, c) for (r, c), ws in cell.items() for w in ws}
    ex, seen = [], set()
    for f in lines("kon.txt"):
        assert len(f) == 9, f
        level, relation, cls, A, B, sentence, answer, options, note = f
        options = [o.strip() for o in options.split(",")]
        assert level in "ABC" and relation in eng and cls in CLASSES, f
        assert sentence.count("___") == 1 and sentence not in seen, f
        seen.add(sentence)
        assert answer in options and 4 <= len(options) <= 5, f
        assert answer.lower() in [w.lower() for w in cell[(relation, cls)]], f"{answer} not in {relation}/{cls}: {f}"
        for o in options:
            assert o.lower() in word_to, f"unknown connector {o}: {f}"
        # no two options with the same relation + class
        low = {o.lower() for o in options}
        if low >= {"aber", "sondern"}:
            low.discard("sondern")  # aber / sondern are not synonyms (sondern needs a negated first clause)
        keys = [word_to[o] for o in low]
        assert len(set(keys)) == len(keys), f"synonyms among options: {f}"
        steps = [
            f"Claims:  A = “{A}”   →   B = “{B}”",
            f"Relation: {note}  → {relation} ({eng[relation]})",
            f"Word order after the blank: {ORDER_TEXT[cls]}",
            f"Table: {relation} × {CLASS_TITLE[cls]} → {', '.join(cell[(relation, cls)])}",
        ]
        shown = f"[{relation}]  {sentence}" if level == "A" else sentence
        ex.append({
            "id": "", "level": level, "type": "connector", "sentence": shown,
            "options": sorted(options, key=str.lower), "answer": answer, "case": relation, "focus": f"{relation} · {cls}",
            "explanation": chain(steps, f"∴ {answer}"),
            "tags": ["connector", relation.lower(), cls.lower()],
            "ref": {"table": "connector", "row": relation, "col": cls},
        })
    table = {"classes": [{"key": c, "title": CLASS_TITLE[c]} for c in CLASSES],
             "rows": [{"key": r, "label": f"{r}", "gloss": e, "cells": cols} for r, e, cols in TABLE]}
    dump("kon.json", finish(ex, "K", 61))
    dump("kon_table.json", table)
    return len(ex), (Counter(x["level"] for x in ex), Counter(x["tags"][1] for x in ex), Counter(x["tags"][2] for x in ex))


def main():
    only = sys.argv[1:] or ["dec", "fuz", "lazy", "kon"]
    for name, fn in (("dec", build_dec), ("fuz", build_fuz), ("lazy", build_lazy), ("kon", build_kon)):
        if name in only:
            print(name, fn())


if __name__ == "__main__":
    main()
