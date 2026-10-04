#!/usr/bin/env python3
"""Generate the verb + preposition section (src/data/vp.json and src/data/vp_chunks.json).

Input : scripts/vp_data.py  (hand-written chunks and example sentences)
Output: vp.json         one exercise per example sentence, the blank is the preposition
        vp_chunks.json  the chunk list shown next to the exercises (grouped by preposition + case)

Usage:  python3 scripts/gen_vp.py
"""
import json
import os
import random
import re
import sys
import zlib
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vp_data import CHUNKS  # noqa: E402

PREPS = ["an", "auf", "aus", "bei", "für", "gegen", "in", "mit", "nach", "über", "um", "von", "vor", "zu"]
CASE_FULL = {"Akk": "Akkusativ", "Dat": "Dativ"}
N_OPTIONS = 8
MARK = re.compile(r"\[(\w+)\]\s*\{([^}]*)\}")


class Chunk:
    def __init__(self, line):
        f = [x.strip() for x in line.split("|")]
        assert len(f) >= 8, f"need 7 fields + sentences: {line[:60]}"
        self.verb, self.prep, self.case, self.level, self.gloss, excl, self.note = f[:7]
        self.sentences = [s for s in f[7:] if s]
        self.excl = {x for x in excl.split(",") if x}
        assert self.prep in PREPS, line[:60]
        assert self.case in CASE_FULL and self.level in "ABC", line[:60]
        assert len(self.sentences) >= 3, f"{self.verb} {self.prep}: at least 3 sentences"
        for s in self.sentences:
            m = MARK.findall(s)
            assert len(m) == 1 and m[0][0] == self.prep, f"bad marker in: {s}"
        self.key = f"{self.verb} {self.prep}"
        self.group = f"{self.prep} + {self.case}"


def explain(c, np, siblings):
    steps = [f"Fixed chunk (the verb decides the preposition): {c.key} + {CASE_FULL[c.case]} = {c.gloss}"]
    if c.note:
        steps.append(c.note)
    elif siblings:
        steps.append("Compare: " + "; ".join(f"{s.key} + {CASE_FULL[s.case]} = {s.gloss}" for s in siblings))
    steps.append(f"After {c.prep} here: {CASE_FULL[c.case]} → {c.prep} {np}")
    return "\n".join([f"{i}. {s}" for i, s in enumerate(steps, 1)] + [f"∴ {c.prep}"])


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(here, "..", "src", "data")
    chunks = [Chunk(l) for l in CHUNKS.strip().splitlines() if l.strip() and not l.strip().startswith("#")]
    assert len({c.key for c in chunks}) == len(chunks), "duplicate chunk: " + str([k for k, v in Counter(c.key for c in chunks).items() if v > 1])
    by_verb = defaultdict(list)
    for c in chunks:
        by_verb[c.verb].append(c)

    rng = random.Random(5)
    exercises, seen = [], set()
    for c in chunks:
        siblings = [s for s in by_verb[c.verb] if s is not c]
        banned = {c.prep} | c.excl | {s.prep for s in siblings}
        if c.case == "Dat":
            # a dative phrase also reads as a time or place ("nach der Arbeit", "bei der Arbeit", "vor der Reise")
            banned |= {"nach", "bei", "vor"}
        pool = [p for p in PREPS if p not in banned]
        for s in c.sentences:
            prep, np = MARK.search(s).groups()
            sentence = MARK.sub(lambda m: "___ " + m.group(2), s)
            assert sentence.count("___") == 1 and sentence not in seen, sentence
            seen.add(sentence)
            # seeded by the sentence itself: editing one chunk never changes the options of another
            pick = random.Random(zlib.crc32(sentence.encode("utf-8"))).sample(pool, min(N_OPTIONS - 1, len(pool)))
            options = sorted(pick + [c.prep], key=lambda p: p.replace("ü", "u"))
            exercises.append({
                "id": "", "level": c.level, "type": "verb_preposition", "sentence": sentence,
                "options": options, "answer": c.prep, "case": CASE_FULL[c.case],
                "focus": f"{c.key} + {c.case}", "explanation": explain(c, np, siblings),
                "tags": [CASE_FULL[c.case].lower(), "verb-preposition", c.prep, c.verb],
                "ref": {"table": "chunks", "row": c.group, "col": c.verb},
            })
    rng.shuffle(exercises)
    for i, x in enumerate(exercises, 1):
        x["id"] = f"V-{i:04d}"

    groups = defaultdict(list)
    for c in chunks:
        groups[c.group].append({"verb": c.verb, "gloss": c.gloss, "level": c.level})
    strip = lambda v: v[5:] if v.startswith("sich ") else v
    listing = []
    for g in sorted(groups, key=lambda g: (g.split(" + ")[0], g)):
        verbs = sorted(groups[g], key=lambda v: (v["level"], strip(v["verb"])))
        listing.append({"key": g, "prep": g.split(" + ")[0], "case": g.split(" + ")[1], "verbs": verbs})

    with open(os.path.join(out_dir, "vp.json"), "w", encoding="utf-8") as fh:
        json.dump(exercises, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    with open(os.path.join(out_dir, "vp_chunks.json"), "w", encoding="utf-8") as fh:
        json.dump(listing, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    lv = Counter(x["level"] for x in exercises)
    print(f"{len(chunks)} chunks in {len(listing)} groups -> {len(exercises)} exercises  levels {dict(lv)}")


if __name__ == "__main__":
    main()
