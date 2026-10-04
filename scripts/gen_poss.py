#!/usr/bin/env python3
"""Generate the ein-word ending section (src/data/poss.json).

The blank is the ending of ein / kein / mein / dein / sein / ihr / unser ("Ich besuche mein___ Freund." -> en).
Reuses the noun lexicon and the case frames of gen_adj.py.

Usage:  python3 scripts/gen_poss.py
"""
import json
import math
import os
import random
import sys
import zlib
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_adj as G  # noqa: E402

NONE = "–"
OPTIONS = [NONE, "e", "em", "en", "er", "es"]
LEVEL_OF = {"Nom": "A", "Akk": "A", "Dat": "B", "Gen": "C"}
PER_CELL = {"A": 30, "B": 30, "C": 20}
STEM_WEIGHT = {"ein": 3, "kein": 2}
STEM_MEANING = {"ein": "a", "kein": "no", "mein": "my", "dein": "your", "sein": "his / its", "ihr": "her", "unser": "our"}


def explain(noun, frame, case, g, stem, ending, phrase):
    gi = G.GENDERS.index(g)
    dw = G.DEF[case][gi]
    if g == "pl":
        s1 = f"Noun: {noun.pl} → plural (all genders share one column)"
    else:
        s1 = f"Noun: {noun.sg} → {G.ARTICLE[g]} {noun.sg} ({G.GENDER_FULL[g]}, singular)"
    s2 = f"Case: {frame.why}"
    s3 = f"{G.CASE_FULL[case]} + {g} → the der-word would be '{dw}'"
    if ending == NONE:
        s4 = (f"'{stem}' is an ein-word ({STEM_MEANING[stem]}): it copies the ending of '{dw}', "
              f"except in Nom m and Nom/Akk n, where it has no ending → '{stem}'")
    else:
        s4 = f"'{stem}' is an ein-word ({STEM_MEANING[stem]}): it copies the ending of '{dw}' → -{ending}"
    steps = [s1, s2, s3, s4]
    last = "no ending" if ending == NONE else f"-{ending}"
    return "\n".join([f"{i}. {s}" for i, s in enumerate(steps, 1)] + [f"∴ {last}  →  {phrase}"])


NOUNS = G.NOUN_LIST


for _n in NOUNS:
    if _n.sg in {"Film", "Pause", "Student", "Studentin"}:
        _n.no_poss_at_all = True  # "mein Film", "meine Studentin" are odd for a learner

KEIN_OK = ("Ich kaufe", "Zum ", "Im Café", "Ich brauche", "Ich suche", "Heute trage", "{NP} {ist/sind} heute im Angebot")
SKIP_FRAMES = ("Während", "{NP} {kommt/kommen} bald.")


def clear(n, case):
    """The blank is the determiner ending, so the noun form must show singular vs plural."""
    if case == "Dat" and n.pl and n.form("Dat", "pl") == n.sg:
        return False  # "Mädchen": keinem / keinen Mädchen
    if case != "Nom" and n.ndecl:
        return False  # Kollegen = Akk/Dat sg and plural
    if case == "Akk" and n.pl == n.sg:
        return False  # "Lehrer": mein Lehrer / meine Lehrer
    if case == "Gen" and n.pl and n.gen == n.pl:
        return False  # "Chefs": des Chefs / der Chefs
    return True


def build():
    out = []
    for case in G.CASES:
        for g in G.GENDERS:
            level = LEVEL_OF[case]
            quota = PER_CELL[level]
            end = G.EIN_END[case][G.GENDERS.index(g)]
            ending = end or NONE
            rng = random.Random(zlib.crc32(f"poss{case}{g}".encode()))
            frames = [f for f in G.FRAME_LIST if f.case == case and not f.tpl.startswith(SKIP_FRAMES)]
            pairs = [(f, n) for f in frames for n in NOUNS if clear(n, case) and G.usable(n, f, "mixed", g)]
            nouns = {n.sg for _, n in pairs}
            cap = max(2, math.ceil(quota / len(nouns)))
            fcap = max(2, math.ceil(quota / len({f.tpl for f, _ in pairs})))
            rng.shuffle(pairs)
            used_n, used_f, seen, made = Counter(), Counter(), set(), 0
            for relax in range(5):
                for f, n in pairs:
                    if made >= quota:
                        break
                    if used_n[n.sg] >= cap + relax or used_f[f.tpl] >= fcap + relax:
                        continue
                    dets = [d for d in G.determiners("mixed", case, g) if G.det_ok(n, f, "mixed", d[0], d[1])
                            and (d[1] != "kein" or any(f.tpl.startswith(k) for k in KEIN_OK))]
                    if not dets:
                        continue
                    pool = [d for d in dets for _ in range(STEM_WEIGHT.get(d[1], 1))]
                    form, stem = rng.choice(pool)
                    noun = n.form(case, g)
                    sentence = G.plural_verb(f.tpl, g).replace("{NP}", f"{stem}___ {noun}")
                    sentence = sentence[0].upper() + sentence[1:]
                    if sentence in seen:
                        continue
                    seen.add(sentence)
                    used_n[n.sg] += 1
                    used_f[f.tpl] += 1
                    made += 1
                    assert sentence.count("___") == 1 and form == stem + end, (sentence, form)
                    out.append({
                        "id": "", "level": level, "type": "ein_word_ending", "sentence": sentence,
                        "options": OPTIONS, "answer": ending, "case": G.CASE_FULL[case],
                        "focus": f"ein-word · {case} · {g}",
                        "explanation": explain(n, f, case, g, stem, ending, f"{form} {noun}"),
                        "tags": ["ein-word-ending", stem, G.CASE_FULL[case].lower(), g],
                        "ref": {"table": "possessive", "row": case, "col": g},
                    })
                if made >= quota:
                    break
    return out


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "data")
    ex = build()
    rng = random.Random(23)
    ex.sort(key=lambda x: x["level"])
    for lv in "ABC":
        idx = [i for i, x in enumerate(ex) if x["level"] == lv]
        part = [ex[i] for i in idx]
        rng.shuffle(part)
        for i, p in zip(idx, part):
            ex[i] = p
    for i, x in enumerate(ex, 1):
        x["id"] = f"E-{i:04d}"
    with open(os.path.join(out_dir, "poss.json"), "w", encoding="utf-8") as fh:
        json.dump(ex, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    cells = Counter((x["tags"][2], x["tags"][3]) for x in ex)
    print(f"{len(ex)} exercises  levels {dict(Counter(x['level'] for x in ex))}  answers {dict(Counter(x['answer'] for x in ex))}")
    print("smallest cells:", sorted(cells.items(), key=lambda kv: kv[1])[:5])


if __name__ == "__main__":
    main()
