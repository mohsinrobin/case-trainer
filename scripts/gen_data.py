#!/usr/bin/env python3
"""Generate the Level A and B exercises (src/data/a.json, b.json).

Every sentence is built from two hand-written tables:
  * a noun lexicon (gender, plural, genitive ending, weak-noun flag, semantic tags)
  * sentence frames (the case-governing verb/preposition, the semantic tag the
    noun must have, and the sentence text with a {N} slot)

A frame is only combined with nouns that carry the tag the frame asks for, so the
result is grammatical AND sensible ("Das Kind spielt", never "Das Bein schreibt").
The answer, the noun form and the explanation all come from the same lexicon
entry, so they cannot disagree with each other.

Usage:  python3 scripts/gen_data.py            # writes src/data/a.json + b.json
        python3 scripts/gen_data.py --report   # coverage report, writes nothing
"""
import json
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lex_a  # noqa: E402
import lex_b  # noqa: E402

OPTIONS = ["das", "dem", "den", "der", "des", "die"]  # fixed order = stable button positions
GENDER_WORD = {"m": "masculine", "f": "feminine", "n": "neuter", "p": "plural"}
BASE = {"m": "der", "f": "die", "n": "das", "p": "die"}
ARTICLE = {
    ("m", "Nominativ"): "der", ("m", "Akkusativ"): "den", ("m", "Dativ"): "dem", ("m", "Genitiv"): "des",
    ("f", "Nominativ"): "die", ("f", "Akkusativ"): "die", ("f", "Dativ"): "der", ("f", "Genitiv"): "der",
    ("n", "Nominativ"): "das", ("n", "Akkusativ"): "das", ("n", "Dativ"): "dem", ("n", "Genitiv"): "des",
    ("p", "Nominativ"): "die", ("p", "Akkusativ"): "die", ("p", "Dativ"): "den", ("p", "Genitiv"): "der",
}
KIND_CASE = {"NS": "Nominativ", "NP": "Nominativ", "AV": "Akkusativ", "AP": "Akkusativ", "AW": "Akkusativ",
             "DV": "Dativ", "DI": "Dativ", "DP": "Dativ", "DW": "Dativ", "GP": "Genitiv", "GA": "Genitiv"}
KIND_TAG = {"NS": "subject", "NP": "predicate", "AV": "verb", "AP": "preposition", "AW": "preposition",
            "DV": "verb", "DI": "verb", "DP": "preposition", "DW": "preposition", "GP": "preposition", "GA": "possession"}
CASES = ["Nominativ", "Akkusativ", "Dativ", "Genitiv"]

GENDER_WEIGHTS = {
    "Nominativ": {"m": .34, "f": .24, "n": .26, "p": .16},
    "Akkusativ": {"m": .42, "f": .20, "n": .22, "p": .16},
    "Dativ":     {"m": .34, "f": .26, "n": .18, "p": .22},
    "Genitiv":   {"m": .32, "f": .26, "n": .26, "p": .16},
}
LEVELS = {
    "A": {"module": lex_a, "counts": {"Nominativ": 400, "Akkusativ": 500, "Dativ": 450, "Genitiv": 150}, "seed": 11,
          "keep": 750, "pron": {"Nominativ": 200, "Akkusativ": 260, "Dativ": 290},
          "pron12": {"Nominativ": 40, "Akkusativ": 90, "Dativ": 120}, "pron3": {"Nominativ": 160, "Akkusativ": 170, "Dativ": 170}},
    "B": {"module": lex_b, "counts": {"Nominativ": 350, "Akkusativ": 400, "Dativ": 400, "Genitiv": 350}, "seed": 22,
          "keep": 750, "pron": {"Nominativ": 200, "Akkusativ": 260, "Dativ": 290},
          "pron12": {"Nominativ": 40, "Akkusativ": 90, "Dativ": 120}, "pron3": {"Nominativ": 160, "Akkusativ": 170, "Dativ": 170}},
}


class Noun:
    def __init__(self, line):
        sg, g, pl, gen, tags = [x.strip() for x in line.split("|")]
        assert g in "mfnp", line
        self.sg, self.g = sg, g
        self.pl = None if pl == "-" else pl
        self.weak = gen[2:] if gen.startswith("W:") else None
        self.gsuf = "" if (gen == "-" or self.weak) else gen
        self.tags = set(tags.split())
        if g == "p":
            self.pl = sg
        if g in "mn" and not self.weak:
            assert self.gsuf, f"genitive ending missing: {line}"

    def genders(self):
        return ["p"] if self.g == "p" else [self.g] + (["p"] if self.pl else [])

    def ambiguous(self, case):
        """Sg and pl look identical in this case (e.g. Lehrer, Mädchen, weak nouns): both 'den Lehrer'
        and 'die Lehrer' would be right, so we do not use the noun with this case at all.
        Nominativ is safe because every subject frame has a verb that shows the number."""
        if case == "Nominativ" or not self.pl or self.g == "p":
            return False
        return self.form(self.g, case) == self.form("p", case)

    def form(self, g, case):
        if g == "p":
            if case == "Dativ" and not self.pl.endswith(("n", "s")):
                return self.pl + "n"
            return self.pl
        if self.weak and case != "Nominativ":
            return self.sg + self.weak
        if case == "Genitiv" and g in "mn":
            return self.sg + self.gsuf
        return self.sg


class Frame:
    def __init__(self, line):
        kind, key, tags, genders, tpl = [x.strip() for x in line.split("|", 4)]
        assert kind in KIND_CASE, line
        self.kind, self.key, self.tpl = kind, key, tpl
        self.case = KIND_CASE[kind]
        self.tags = set(tags.split("|"))
        self.genders = "mfnp" if genders == "*" else genders
        assert tpl.count("{N}") == 1, line
        if kind in ("NS", "NP"):
            assert "<" in tpl, "subject frame needs <sg|pl> verb agreement: " + line


def parse(text, cls):
    return [cls(l) for l in text.strip().splitlines() if l.strip() and not l.strip().startswith("#")]


def trigger(f):
    """Step 1 of the explanation: what decides the case."""
    k = f.key
    return {
        "NS": f"the noun is the subject of {k} → Nominativ",
        "NP": f"after {k} the noun says who/what the subject is → Nominativ",
        "AV": f"{k} takes a direct object → Akkusativ",
        "AP": f"{k} is always followed by Akkusativ",
        "AW": f"{k} + movement (wohin?) → Akkusativ",
        "DV": f"{k} takes a Dativ object → Dativ",
        "DI": f"{k}: the receiver is the Dativ object → Dativ",
        "DP": f"{k} is always followed by Dativ",
        "DW": f"{k} + position (wo?) → Dativ",
        "GP": f"{k} is always followed by Genitiv",
        "GA": f"owner of the {k} (whose?) → Genitiv",
    }[f.kind]


def explain(f, n, g, case, form):
    """A short proof: trigger -> noun gender -> article rule -> answer."""
    base, art = BASE[g], ARTICLE[(g, case)]
    gw = GENDER_WORD[g]
    name = n.pl if g == "p" else n.sg
    if g == "p" and n.g != "p":
        who = f"{n.pl} is plural (singular: {n.sg})"
    else:
        who = f"{name} is {gw}"
    steps = [trigger(f), f"{who} → the article is {base}"]
    if base == art:
        steps.append(f"{case} + {gw}: {base} stays {art}")
    else:
        steps.append(f"{case} + {gw}: {base} → {art}")
    # what happens to the noun itself
    if g == "p" and case == "Dativ" and form != n.pl:
        steps.append(f"Dativ plural adds -n to the noun: {n.pl} → {form}")
    elif g in "mn" and case == "Genitiv" and not n.weak:
        steps.append(f"Genitiv {gw} adds -{form[len(n.sg):]} to the noun: {n.sg} → {form}")
    if n.weak and g != "p" and case != "Nominativ":
        steps.append(f"{n.sg} is a weak (n-)noun, so it also gets -{n.weak}: {n.sg} → {form}")
    lines = [f"{i}. {s}" for i, s in enumerate(steps, 1)]
    lines.append(f"∴ {art}")
    return "\n".join(lines)


# ======================================================================
#  Personal-pronoun exercises
# ======================================================================
PRON = {  # row of the reference table -> (Nominativ, Akkusativ, Dativ)
    "ich": ("ich", "mich", "mir"), "du": ("du", "dich", "dir"), "er": ("er", "ihn", "ihm"),
    "sie": ("sie", "sie", "ihr"), "es": ("es", "es", "ihm"), "wir": ("wir", "uns", "uns"),
    "ihr": ("ihr", "euch", "euch"), "sie/Sie": ("sie", "sie", "ihnen"),
}
GENDER_ROW = {"m": "er", "f": "sie", "n": "es", "p": "sie/Sie"}
GENDER_PRON_GLOSS = {"er": "er (he/it)", "sie": "sie (she/it)", "es": "es (it)", "sie/Sie": "sie (they)"}
CASE_IDX = {"Nominativ": 0, "Akkusativ": 1, "Dativ": 2}
OPT3 = ["er", "es", "ihm", "ihn", "ihnen", "ihr", "sie"]
OPT12_OBLIQUE = ["dich", "dir", "euch", "mich", "mir", "uns"]
OPT12_NOM = ["du", "ich", "ihr", "wir"]
PERSON_INFO = {"ich": "1st person singular", "du": "2nd person singular", "wir": "1st person plural", "ihr": "2nd person plural"}
PERSON_CAP = {"ich": "Ich", "du": "Du", "wir": "Wir", "ihr": "Ihr"}
SEIN = {"ich": "bin", "du": "bist", "wir": "sind", "ihr": "seid"}
NOM_ARTICLE = {"m": "der", "f": "die", "n": "das", "p": "die"}
LEADINS3 = ["Das <ist|sind> {R}.", "Hier <ist|sind> {R}.", "Dort <ist|sind> {R}."]
PREP_KINDS = ("AP", "AW", "DP", "DW")
PRON_WEIGHTS = {"m": .30, "f": .25, "n": .20, "p": .25}
SUBORDINATORS = {"sobald", "dass", "bis", "wann", "weil", "wenn", "ob"}
ADVERBS = {"bitte", "dringend", "immer", "noch", "oft", "gern", "gerne", "nie", "schon", "fast", "auch", "nur", "jetzt",
           "leider", "sofort", "gleich", "endlich", "lieber", "heute", "gestern", "morgen", "zuerst", "wieder", "bald",
           "zurzeit", "dann", "hier", "dort", "ganz", "sehr"}
FIXED_SUBJECT_PRONOUNS = {"er", "sie", "es"}
COLLECTIVES = {"Team", "Mannschaft", "Familie", "Klasse", "Regierung", "Partei", "Verein", "Abteilung"}
CONCRETE = {"person", "animal", "thing", "obj", "furniture", "clothes", "vehicle", "building", "room", "food", "drink",
            "plant", "media", "device", "part", "tech", "gadget", "doc", "luggage", "goods", "home"}
NOT_BEFORE_PRONOUN = {"mir", "dir", "uns", "euch", "sich", "ihm", "ihr", "mich", "dich", "ihn", "ihnen", "Ihnen",
                      "der", "die", "das", "den", "dem", "des", "ein", "eine", "einen", "einem", "einer",
                      "mein", "meine", "meinen", "meinem", "meiner", "unser", "unsere", "dein", "deine"}


def alt(text, plural):
    return re.sub(r"<([^|>]*)\|([^>]*)>", lambda m: m.group(2) if plural else m.group(1), text)


def pronoun_ok(f):
    """Can the noun slot of this frame be replaced by a pronoun without sounding odd?"""
    if f.kind in ("GA", "GP", "NP") or f.key == "gegenüber" or "<war|waren>" in f.tpl:
        return False
    if f.tpl.startswith("Wo "):          # "Hier ist X. Wo ist er?" contradicts itself
        return False
    pre = f.tpl.split("{N}")[0].split()
    # a fixed er/sie/es in the sentence could be the same person as the blank -> reflexive clash
    if any(t.lower().strip(",") in FIXED_SUBJECT_PRONOUNS for t in pre):
        return False
    if not pre:
        return f.kind == "NS"
    last = pre[-1]
    if f.kind == "NS":
        return last.endswith(">") or last.lower() in SUBORDINATORS
    return not (last in NOT_BEFORE_PRONOUN or last[0].isupper() or last.lower() in ADVERBS)


def pron_trigger(f):
    if f.key == "gegenüber":
        return "gegenüber takes Dativ (a pronoun comes before it: mir gegenüber)"
    return trigger(f).replace("the noun", "the pronoun")


def pron_explain3(f, n, g, case, ans):
    row = GENDER_ROW[g]
    nom = PRON[row][0]
    art = NOM_ARTICLE[g]
    noun = n.pl if g == "p" else n.sg
    steps = [pron_trigger(f), f"{art} {noun} is {GENDER_WORD[g]} → the pronoun is {GENDER_PRON_GLOSS[row]}"]
    if nom == ans:
        steps.append(f"{case} of {nom}: {nom} stays {ans}")
    else:
        steps.append(f"{case} of {nom}: {nom} → {ans}")
    return "\n".join([f"{i}. {s}" for i, s in enumerate(steps, 1)] + [f"∴ {ans}"])


def pron_explain12(f, person, case, ans):
    nom = PRON[person][0]
    steps = [pron_trigger(f), f"{PERSON_CAP[person]} = {PERSON_INFO[person]} → the pronoun is {person}"]
    steps.append(f"{case} of {nom}: {nom} → {ans}" if nom != ans else f"{case} of {nom}: {nom} stays {ans}")
    return "\n".join([f"{i}. {s}" for i, s in enumerate(steps, 1)] + [f"∴ {ans}"])


def pron_ex(level, sentence, ans, case, options, focus, explanation, tags, row):
    return {
        "id": "", "level": level, "type": "personal_pronoun", "sentence": sentence, "options": list(options),
        "answer": ans, "case": case, "focus": focus, "explanation": explanation, "tags": tags,
        "ref": {"table": "pronoun", "row": row, "col": CASE_ABBR[case]},
    }


def build_pronouns(level, cfg, used):
    mod = cfg["module"]
    nouns = parse(mod.NOUNS, Noun)
    frames = parse(mod.FRAMES, Frame)
    p12 = parse(mod.PRON_FRAMES, Frame)
    preds = [x.strip() for x in mod.PRON_PREDICATES.strip().splitlines() if x.strip()]
    dialogues = [x.split("|") for x in mod.PRON_DIALOGUES.strip().splitlines() if x.strip()]
    rng = random.Random(cfg["seed"] + 100)
    want = cfg["pron"]
    out = []

    # -- 1st / 2nd person, Nominativ: short dialogues ---------------------------------
    rng.shuffle(dialogues)
    n_dia = min(cfg["pron12"]["Nominativ"], len(dialogues))
    for ans, asked, tpl, verb in dialogues[:n_dia]:
        sent = tpl.replace("{P}", "___")
        assert sent.count("___") == 1 and sent not in used, sent
        used.add(sent)
        expl = "\n".join([
            "1. Nominativ: the pronoun is the subject of the reply",
            f"2. The question is addressed to {asked}, so the speaker answers as {ans} ({PERSON_INFO[ans]})",
            f"3. The verb form {verb} goes with {ans}",
            f"∴ {ans}"])
        out.append(pron_ex(level, sent, ans, "Nominativ", OPT12_NOM, f"Nominativ pronoun {ans}", expl,
                           ["nominativ", "personal-pronoun", PERSON_INFO[ans].split()[0] + "-person", "dialogue"], ans))

    # -- 1st / 2nd person, Akkusativ / Dativ ------------------------------------------
    persons = ["ich", "du", "wir", "ihr"]
    for case in ("Akkusativ", "Dativ"):
        pool = [f for f in p12 if f.case == case]
        target = cfg["pron12"][case]
        f_used, made = Counter(), 0
        guard = 0
        while made < target and guard < target * 40:
            guard += 1
            person = persons[made % 4]
            f = min(pool, key=lambda x: (f_used[x.key + x.tpl], rng.random()))
            pred = rng.choice(preds)
            lead = f"{PERSON_CAP[person]} {SEIN[person]} {pred}."
            sent = lead + " " + f.tpl.replace("{N}", "___")
            if sent in used:
                continue
            used.add(sent)
            f_used[f.key + f.tpl] += 1
            ans = PRON[person][CASE_IDX[case]]
            out.append(pron_ex(level, sent, ans, case, OPT12_OBLIQUE, f"{case} pronoun {person}",
                               pron_explain12(f, person, case, ans),
                               [case.lower(), "personal-pronoun", PERSON_INFO[person].split()[0] + "-person", KIND_TAG[f.kind]], person))
            made += 1

    # -- 3rd person: reuse the article frames, name the referent in a lead-in sentence ---
    noun_used = Counter()
    noun_cap = math.ceil(sum(cfg["pron3"].values()) / len(nouns) * 3)
    for case in ("Nominativ", "Akkusativ", "Dativ"):
        target = cfg["pron3"][case] if case != "Nominativ" else want["Nominativ"] - n_dia
        cands = []
        for fi, f in enumerate(frames):
            if f.case != case or not pronoun_ok(f):
                continue
            allowed = "mfnp" if f.genders == "fp" else f.genders
            for ni, n in enumerate(nouns):
                if not (f.tags & n.tags):
                    continue
                if f.kind in PREP_KINDS and not (n.tags & {"person", "animal"}):
                    continue
                for g in n.genders():
                    if g not in allowed or (g == "n" and "person" in n.tags):
                        continue
                    if g == "n" and f.kind in PREP_KINDS:           # "um es" -> German wants a da-compound
                        continue
                    if g != "p" and n.sg in COLLECTIVES:            # Team/Familie ... -> "ihnen" is also natural
                        continue
                    cands.append((fi, ni, g))
        nfr = len({c[0] for c in cands})
        frame_cap = max(3, math.ceil(target / max(nfr, 1) * 1.6))
        f_used = Counter()
        quotas = {g: round(target * w) for g, w in PRON_WEIGHTS.items()}
        quotas["m"] += target - sum(quotas.values())
        chosen = 0

        def take(genders, count):
            nonlocal chosen
            pool = [c for c in cands if c[2] in genders]
            rng.shuffle(pool)
            got = 0
            while got < count and pool:
                best, best_s = None, None
                for c in pool:
                    fi, ni, g = c
                    if f_used[fi] >= frame_cap or noun_used[ni] >= noun_cap:
                        continue
                    s = f_used[fi] / frame_cap + noun_used[ni] / noun_cap + rng.random() * 0.35
                    if best_s is None or s < best_s:
                        best, best_s = c, s
                if best is None:
                    break
                pool.remove(best)
                fi, ni, g = best
                f, n = frames[fi], nouns[ni]
                leads = LEADINS3 if (n.tags & CONCRETE) else LEADINS3[:1]
                lead = alt(rng.choice(leads).replace("{R}", f"{NOM_ARTICLE[g]} {n.pl if g == 'p' else n.sg}"), g == "p")
                sent = lead + " " + alt(f.tpl.replace("{N}", "___"), g == "p")
                if sent in used:
                    continue
                used.add(sent)
                f_used[fi] += 1
                noun_used[ni] += 1
                row = GENDER_ROW[g]
                ans = PRON[row][CASE_IDX[case]]
                out.append(pron_ex(level, sent, ans, case, OPT3, f"{case} pronoun {row}",
                                   pron_explain3(f, n, g, case, ans),
                                   [case.lower(), "personal-pronoun", "3rd-person", KIND_TAG[f.kind]], row))
                got += 1
                chosen += 1
            return got

        short = 0
        for g, q in quotas.items():
            short += q - take(g, q)
        if short:
            take("mfnp", short)
        if chosen < target:
            frame_cap += 3
            take("mfnp", target - chosen)
        if chosen < target:
            print(f"WARNING level {level} pronoun {case}: only {chosen}/{target}")
    return out


def subsample_articles(ex, keep, seed):
    """Keep `keep` of the (already reviewed) article exercises, same case/gender mix."""
    rng = random.Random(seed + 7)
    groups = defaultdict(list)
    for x in ex:
        groups[(x["case"], x["focus"].split()[1])].append(x)
    quota = {k: len(v) * keep / len(ex) for k, v in groups.items()}
    take = {k: int(q) for k, q in quota.items()}
    rest = keep - sum(take.values())
    for k in sorted(quota, key=lambda k: quota[k] - take[k], reverse=True)[:rest]:
        take[k] += 1
    picked = []
    for k, v in groups.items():
        picked += rng.sample(v, take[k])
    return picked


def build_level(level, cfg, used_sentences, report):
    mod = cfg["module"]
    nouns = parse(mod.NOUNS, Noun)
    frames = parse(mod.FRAMES, Frame)
    rng = random.Random(cfg["seed"])
    assert len({n.sg for n in nouns}) == len(nouns), "duplicate nouns: " + str([k for k, v in Counter(n.sg for n in nouns).items() if v > 1])

    # every (frame, noun, gender) combination that is grammatical + sensible
    cands = defaultdict(list)
    per_frame = Counter()
    for fi, f in enumerate(frames):
        for ni, n in enumerate(nouns):
            if not (f.tags & n.tags) or n.ambiguous(f.case) or (f.kind == "GA" and n.sg == f.key):
                continue
            for g in n.genders():
                if g in f.genders:
                    cands[f.case].append((fi, ni, g))
                    per_frame[fi] += 1

    dead = [(f.kind, f.key, sorted(f.tags)) for i, f in enumerate(frames) if per_frame[i] == 0]
    if dead:
        raise SystemExit(f"Level {level}: frames with no matching noun: {dead}")
    if report:
        print(f"== Level {level}: {len(nouns)} nouns, {len(frames)} frames")
        for c in CASES:
            print(f"  {c}: {sum(1 for f in frames if f.case == c)} frames, {len(cands[c])} combos")
        thin = [(frames[i].kind, frames[i].key, sorted(frames[i].tags), per_frame[i]) for i in range(len(frames)) if per_frame[i] < 4]
        print("  frames with <4 combos:", len(thin))
        for t in thin:
            print("    ", t)
        for c in CASES:
            gc = Counter(g for _, _, g in cands[c])
            print(f"  {c} combos by gender:", dict(gc))

    total = sum(cfg["counts"].values())
    noun_cap = math.ceil(total / len(nouns) * 3)
    exercises = []
    noun_used = Counter()
    for case in CASES:
        target = cfg["counts"][case]
        pool_all = cands[case]
        nframes = len({fi for fi, _, _ in pool_all})
        frame_cap = max(3, math.ceil(target / max(nframes, 1) * 1.6))
        frame_used = Counter()
        chosen = []
        quotas = {g: round(target * w) for g, w in GENDER_WEIGHTS[case].items()}
        quotas["m"] += target - sum(quotas.values())

        def take(genders, count):
            picked = 0
            pool = [c for c in pool_all if c[2] in genders]
            rng.shuffle(pool)
            while picked < count and pool:
                best, best_s = None, None
                for c in pool:
                    fi, ni, g = c
                    if frame_used[fi] >= frame_cap or noun_used[ni] >= noun_cap:
                        continue
                    s = frame_used[fi] / frame_cap + noun_used[ni] / noun_cap + rng.random() * 0.35
                    if best_s is None or s < best_s:
                        best, best_s = c, s
                if best is None:
                    break
                pool.remove(best)
                fi, ni, g = best
                sent = render(frames[fi], nouns[ni], g, case)
                if sent in used_sentences:
                    continue
                used_sentences.add(sent)
                frame_used[fi] += 1
                noun_used[ni] += 1
                chosen.append((fi, ni, g, sent))
                picked += 1
            return picked

        short = 0
        for g, q in quotas.items():
            short += q - take(g, q)
        if short:  # a gender ran out of combos: fill from anything left
            take("mfnp", short)
        if len(chosen) < target:
            frame_cap += 3
            take("mfnp", target - len(chosen))
        if len(chosen) < target:
            print(f"WARNING level {level} {case}: only {len(chosen)}/{target}")
        for fi, ni, g, sent in chosen:
            exercises.append(make_ex(level, frames[fi], nouns[ni], g, case, sent))

    rng.shuffle(exercises)
    # Hand corrections found in the final proof-read (see POST_FIXES in the lexicon file).
    # Applied after selection so that the reviewed set of sentences stays exactly as it was.
    for ex in exercises:
        fix = getattr(mod, "POST_FIXES", {}).get(ex["sentence"])
        if fix:
            old, new = fix
            ex["sentence"] = ex["sentence"].replace(old, new)
            ex["explanation"] = ex["explanation"].replace(old, new)
            assert ex["sentence"] not in used_sentences, ex["sentence"]
            used_sentences.add(ex["sentence"])
    for i, ex in enumerate(exercises, 1):
        ex["id"] = f"{level}-{i:04d}"
    return exercises


def render(f, n, g, case):
    s = f.tpl.replace("{N}", "___ " + n.form(g, case))
    s = re.sub(r"<([^|>]*)\|([^>]*)>", lambda m: m.group(2) if g == "p" else m.group(1), s)
    assert s.count("___") == 1, s
    return s


CASE_ABBR = {"Nominativ": "Nom", "Akkusativ": "Akk", "Dativ": "Dat", "Genitiv": "Gen"}
COL_REF = {"m": "m", "f": "f", "n": "n", "p": "pl"}


def make_ex(level, f, n, g, case, sent):
    form = n.form(g, case)
    answer = ARTICLE[(g, case)]
    tags = [case.lower(), GENDER_WORD[g], "definite-article", KIND_TAG[f.kind]]
    if sent.rstrip().endswith("?"):
        tags.append("question")
    return {
        "id": "",
        "level": level,
        "type": "definite_article",
        "sentence": sent,
        "options": list(OPTIONS),
        "answer": answer,
        "case": case,
        "focus": f"{case} {GENDER_WORD[g]}",
        "explanation": explain(f, n, g, case, form),
        "tags": tags,
        "ref": {"table": "article", "row": CASE_ABBR[case], "col": COL_REF[g]},
    }


def main():
    report = "--report" in sys.argv
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "data")
    used = set()
    for level, cfg in LEVELS.items():
        articles = build_level(level, cfg, used, report)
        if report:
            continue
        articles = subsample_articles(articles, cfg["keep"], cfg["seed"])
        pronouns = build_pronouns(level, cfg, used)
        ex = articles + pronouns
        random.Random(cfg["seed"] + 3).shuffle(ex)
        for i, x in enumerate(ex, 1):
            x["id"] = f"{level}-{i:04d}"
        path = os.path.join(out_dir, f"{level.lower()}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(ex, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        c = Counter((e_["type"], e_["case"]) for e_ in ex)
        print(f"{level}: wrote {len(ex)} -> {path}")
        for k in sorted(c):
            print("   ", k, c[k])


if __name__ == "__main__":
    main()
