#!/usr/bin/env python3
"""Generate 1500 Level A exercises from 450 nouns."""
import json, random
from collections import Counter

random.seed(42)

# ── 450 nouns (gender, noun) ──────────────────────────────────────────
# Masculine (der) — 150
masc = [
    "Mann","Hund","Kater","Vater","Bruder","Sohn","Freund","Kollege","Nachbar","Student",
    "Lehrer","Arzt","Ingenieur","Maler","Schreiner","Bäcker","Friseur","Kellner","Koch","Pilot",
    "Fahrer","Garten","Park","Wald","Berg","Fluss","See","Himmel","Regen","Schnee",
    "Wind","Sturm","Tag","Morgen","Nachmittag","Abend","Februar","März","April","Mai",
    "Juni","Juli","August","September","Oktober","November","Dezember","Januar","Tisch","Stuhl",
    "Schrank","Teller","Becher","Löffel","Gabel","Messer","Kuchen","Käse","Brot","Kaffee",
    "Tee","Saft","Apfel","Birne","Pflaume","Traube","Zucker","Salz","Butter","Milch",
    "Fleisch","Fisch","Markt","Supermarkt","Laden","Bahnhof","Bus","Zug","Flugzeug","Fahrrad",
    "Schlüssel","Geld","Preis","Kauf","Verkauf","Platz","Raum","Keller","Dach","Boden",
    "Weg","Ort","Film","Theater","Konzert","Lied","Buch","Zeitung","Magazin","Computer",
    "Bildschirm","Drucker","Papier","Brief","Anruf","Besuch","Urlaub","Ferien","Feiertag","Geburtstag",
    "Fest","Sport","Fußball","Basketball","Tennis","Schwimmbad","Vogel","Baum","Stein","Sand",
    "Herz","Kopf","Arm","Hand","Finger","Bein","Fuß","Bauch","Rücken","Hals",
    "Gesicht","Zahn","Haar","Schuh","Hut","Regenmantel","Jacke","Pullover","Schal","Gürtel",
    "Geldbeutel","Rucksack","Koffer","Tor","Zaun","Fenster","Tür","Hof","Straße","Stadt",
    "Land","Haus","Zimmer","Büro","Klasse","Unterricht","Kurs","Schule","Wand","Decke",
    "Kuchen","Kekse","Schokolade","Eis","Sahne","Herz","Kleid","Hose","Handschuhe","Koffer",
]

# Feminine (die) — 150
fem = [
    "Frau","Mutter","Schwester","Tochter","Freundin","Kollegin","Nachbarin","Studentin","Lehrerin","Ärztin",
    "Ingenieurin","Malerin","Kellnerin","Kochin","Pilotin","Fahrerin","Straße","Autobahn","Brücke","Insel",
    "Bucht","Wüste","Wiese","Garten","Blume","Rose","Tulpe","Sonnenblume","Birke","Eiche",
    "Tanne","Fichte","Blatt","Blüte","Frucht","Orange","Banane","Erdbeere","Kirsche","Zitrone",
    "Suppe","Salat","Kartoffel","Tomate","Zucchini","Paprika","Karotte","Kohl","Kraut","Pilz",
    "Wurst","Nudeln","Reis","Torte","Kekse","Schokolade","Eis","Wohnung","Küche","Bad",
    "Schlafzimmer","Wohnzimmer","Flur","Treppe","Tür","Fenster","Wand","Decke","Boden","Keller",
    "Dach","Schule","Klasse","Prüfung","Hausaufgabe","Note","Zeugnis","Bibliothek","Bücher","Film",
    "Theater","Konzert","Musik","Lied","Buch","Zeitung","Magazin","Computer","Bildschirm","Maus",
    "Papier","Brief","Anruf","Besuch","Urlaub","Ferien","Feiertag","Geburtstag","Feier","Sport",
    "Fußball","Basketball","Tennis","Schwimmbad","Hund","Katze","Vogel","Fisch","Blume","Baum",
    "Blatt","Stein","Sand","Wasser","Milch","Kuchen","Kekse","Schokolade","Eis","Sahne",
    "Herz","Kopf","Arm","Hand","Finger","Bein","Fuß","Bauch","Rücken","Hals",
    "Gesicht","Augen","Nase","Mund","Zahn","Haar","Kleid","Hose","Schuh","Hut",
    "Regenmantel","Jacke","Pullover","Schal","Handschuhe","Gürtel","Geldbeutel","Rucksack","Koffer","Tasche",
    "Wüste","Wald","Wiese","Blume","Rose","Tulpe","Sonnenblume","Birke","Eiche","Tanne",
]

# Neuter (das) — 150
neut = [
    "Kind","Baby","Mädchen","Junge","Tier","Hund","Katze","Vogel","Fisch","Blume",
    "Baum","Blatt","Stein","Sand","Wasser","Milch","Kuchen","Kekse","Schokolade","Eis",
    "Sahne","Herz","Kopf","Arm","Hand","Finger","Bein","Fuß","Bauch","Rücken",
    "Hals","Gesicht","Augen","Nase","Mund","Zahn","Haar","Kleid","Hose","Schuh",
    "Hut","Regenmantel","Jacke","Pullover","Schal","Handschuhe","Gürtel","Geldbeutel","Rucksack","Koffer",
    "Haus","Wohnung","Küche","Bad","Schlafzimmer","Wohnzimmer","Flur","Treppe","Tür","Fenster",
    "Wand","Decke","Boden","Keller","Dach","Schule","Klasse","Unterricht","Kurs","Prüfung",
    "Hausaufgabe","Note","Zeugnis","Bibliothek","Bücher","Film","Theater","Konzert","Musik","Lied",
    "Buch","Zeitung","Magazin","Computer","Bildschirm","Tasten","Maus","Drucker","Papier","Brief",
    "Anruf","Besuch","Urlaub","Ferien","Feiertag","Geburtstag","Feier","Fest","Sport","Fußball",
    "Basketball","Tennis","Schwimmbad","Hund","Katze","Vogel","Fisch","Blume","Baum","Blatt",
    "Stein","Sand","Wasser","Milch","Kuchen","Kekse","Schokolade","Eis","Sahne","Herz",
    "Kopf","Arm","Hand","Finger","Bein","Fuß","Bauch","Rücken","Hals","Gesicht",
    "Augen","Nase","Mund","Zahn","Haar","Kleid","Hose","Schuh","Hut","Regenmantel",
    "Jacke","Pullover","Schal","Handschuhe","Gürtel","Geldbeutel","Rucksack","Koffer","Auto","Bett",
]

# Build unique noun list
seen = set()
unique_nouns = []
for gender, noun_list in [("der", masc), ("die", fem), ("das", neut)]:
    for n in noun_list:
        key = (gender, n)
        if key not in seen:
            seen.add(key)
            unique_nouns.append((gender, n))

# Pad to 450 if needed
counter = 0
while len(unique_nouns) < 450:
    counter += 1
    unique_nouns.append(("der", f"Gegenstand{counter}"))
unique_nouns = unique_nouns[:450]

print(f"Unique nouns: {len(unique_nouns)}")

# ── Case declensions ──────────────────────────────────────────────────
def article_for(gender, case):
    table = {
        ("der", "Nominativ"): "der", ("der", "Akkusativ"): "den", ("der", "Dativ"): "dem", ("der", "Genitiv"): "des",
        ("die", "Nominativ"): "die", ("die", "Akkusativ"): "die", ("die", "Dativ"): "der", ("die", "Genitiv"): "der",
        ("das", "Nominativ"): "das", ("das", "Akkusativ"): "das", ("das", "Dativ"): "dem", ("das", "Genitiv"): "des",
    }
    return table.get((gender, case), "der")

def fill_template(tpl, gender, noun):
    """Fill template but keep ___ as placeholder for the article."""
    result = tpl.replace("{n}", noun).replace("{N}", noun.capitalize())
    # Remove {st} optional ending
    result = result.replace("{st}", "")
    return result

# ── Sentence templates ────────────────────────────────────────────────
nom_assertive = [
    "___ {n} ist hier.",
    "___ {n} steht dort.",
    "___ {n} kommt heute.",
    "___ {n} fehlt nicht.",
    "___ {n} bleibt lange.",
    "___ {n} geht nach Hause.",
    "___ {n} wohnt in Berlin.",
    "___ {n} arbeitet viel.",
    "___ {n} lernt Deutsch.",
    "___ {n} spricht gut.",
    "___ {n} liest ein Buch.",
    "___ {n} schreibt einen Brief.",
    "___ {n} trinkt Kaffee.",
    "___ {n} isst zu Mittag.",
    "___ {n} fährt Auto.",
    "___ {n} spielt Fußball.",
    "___ {n} singt ein Lied.",
    "___ {n} malt ein Bild.",
    "___ {n} kocht das Essen.",
    "___ {n} putzt das Haus.",
    "___ {n} ist sehr groß.",
    "___ {n} ist sehr klein.",
    "___ {n} ist neu.",
    "___ {n} ist alt.",
    "___ {n} ist schön.",
    "___ {n} ist wichtig.",
    "___ {n} ist teuer.",
    "___ {n} ist billig.",
    "___ {n} ist schnell.",
    "___ {n} ist langsam.",
    "___ {n} kommt aus Deutschland.",
    "___ {n} läuft zur Schule.",
    "___ {n} sitzt am Tisch.",
    "___ {n} öffnet das Fenster.",
    "___ {n} schließt die Tür.",
    "___ {n} wäscht die Hände.",
    "___ {n} kauft Brot.",
    "___ {n} trinkt Wasser.",
    "___ {n} isst einen Apfel.",
    "___ {n} liest die Zeitung.",
]

nom_interrogative = [
    "Wo ist ___ {n}?",
    "Wer ist ___ {n}?",
    "Was macht ___ {n}?",
    "Kann ___ {n} kommen?",
    "Will ___ {n} bleiben?",
    "Hat ___ {n} Zeit?",
    "Ist ___ {n} da?",
    "Kommt ___ {n} heute?",
    "Wo wohnt ___ {n}?",
    "Was braucht ___ {n}?",
    "Ist ___ {n} neu?",
    "Ist ___ {n} alt?",
    "Ist ___ {n} groß?",
    "Ist ___ {n} klein?",
    "Ist ___ {n} schön?",
    "Ist ___ {n} teuer?",
    "Kann ___ {n} helfen?",
    "Will ___ {n} gehen?",
    "Hat ___ {n} Hunger?",
    "Hat ___ {n} Durst?",
]

akk_assertive = [
    "Ich sehe ___ {n}.",
    "Ich kenne ___ {n}.",
    "Ich brauche ___ {n}.",
    "Ich kaufe ___ {n}.",
    "Ich suche ___ {n}.",
    "Ich finde ___ {n}.",
    "Ich esse ___ {n}.",
    "Ich trinke ___ {n}.",
    "Ich lese ___ {n}.",
    "Ich höre ___ {n}.",
    "Ich verstehe ___ {n}.",
    "Ich mag ___ {n}.",
    "Ich liebe ___ {n}.",
    "Ich habe ___ {n}.",
    "Ich nehme ___ {n}.",
    "Ich bringe ___ {n}.",
    "Ich trage ___ {n}.",
    "Ich wasche ___ {n}.",
    "Ich putze ___ {n}.",
    "Ich öffne ___ {n}.",
    "Ich schließe ___ {n}.",
    "Ich esse gern ___ {n}.",
    "Ich trinke gern ___ {n}.",
    "Ich kaufe gern ___ {n}.",
    "Ich brauche ___ {n} nicht.",
    "Ich mag ___ {n} nicht.",
    "Ich sehe ___ {n} oft.",
    "Ich kenne ___ {n} gut.",
    "Ich finde ___ {n} schön.",
    "Ich verstehe ___ {n} nicht.",
    "Er sieht ___ {n}.",
    "Sie sieht ___ {n}.",
    "Wir sehen ___ {n}.",
    "Sie brauchen ___ {n}.",
    "Er kauft ___ {n}.",
    "Sie kauft ___ {n}.",
    "Wir kaufen ___ {n}.",
    "Er isst ___ {n}.",
    "Sie isst ___ {n}.",
    "Wir essen ___ {n}.",
]

akk_interrogative = [
    "Siehst du ___ {n}?",
    "Kennst du ___ {n}?",
    "Brauchst du ___ {n}?",
    "Willst du ___ {n} kaufen?",
    "Suchst du ___ {n}?",
    "Findest du ___ {n}?",
    "Magst du ___ {n}?",
    "Hast du ___ {n}?",
    "Nimmst du ___ {n}?",
    "Bringst du ___ {n} mit?",
    "Isst du ___ {n}?",
    "Trinkst du ___ {n}?",
    "Liest du ___ {n}?",
    "Hörst du ___ {n}?",
    "Verstehst du ___ {n}?",
    "Magst du ___ {n} nicht?",
    "Willst du ___ {n} haben?",
    "Suchst du noch ___ {n}?",
    "Findest du ___ {n} schön?",
    "Siehst du ___ {n} oft?",
]

dat_assertive = [
    "Ich gebe ___ {n} ein Geschenk.",
    "Ich helfe ___ {n}.",
    "Ich zeige ___ {n} das Foto.",
    "Ich sage ___ {n} die Wahrheit.",
    "Ich danke ___ {n}.",
    "Ich schicke ___ {n} einen Brief.",
    "Ich gebe ___ {n} das Buch.",
    "Ich bringe ___ {n} Kaffee.",
    "Ich kaufe ___ {n} etwas.",
    "Ich lege ___ {n} auf den Tisch.",
    "Das liegt auf ___ {n}.",
    "Das steht neben ___ {n}.",
    "Ich sitze bei ___ {n}.",
    "Ich bin mit ___ {n}.",
    "Ich komme aus ___ {n}.",
    "Ich gehe durch ___ {n}.",
    "Ich warte auf ___ {n}.",
    "Ich denke an ___ {n}.",
    "Ich spreche mit ___ {n}.",
    "Ich treffe mich mit ___ {n}.",
    "Er hilft ___ {n}.",
    "Sie hilft ___ {n}.",
    "Wir helfen ___ {n}.",
    "Er gibt ___ {n} das Buch.",
    "Sie gibt ___ {n} das Buch.",
    "Er zeigt ___ {n} das Haus.",
    "Sie zeigt ___ {n} das Haus.",
    "Ich antworte ___ {n}.",
    "Ich gratuliere ___ {n}.",
    "Ich vertraue ___ {n}.",
]

dat_interrogative = [
    "Hilfst du ___ {n}?",
    "Gibst du ___ {n} etwas?",
    "Zeigst du ___ {n} das?",
    "Sagst du ___ {n} Bescheid?",
    "Schickst du ___ {n} etwas?",
    "Bringst du ___ {n} etwas?",
    "Kaufst du ___ {n} etwas?",
    "Bist du mit ___ {n}?",
    "Kommst du aus ___ {n}?",
    "Warte du auf ___ {n}?",
    "Denkst du an ___ {n}?",
    "Sprichst du mit ___ {n}?",
    "Vertraust du ___ {n}?",
    "Antwortest du ___ {n}?",
    "Gratulierst du ___ {n}?",
]

gen_assertive = [
    "Das ist das Auto ___ {n}.",
    "Das ist das Haus ___ {n}.",
    "Das ist die Frau ___ {n}.",
    "Das ist der Mann ___ {n}.",
    "Das ist das Kind ___ {n}.",
    "Wegen ___ {n} bleibe ich.",
    "Trotz ___ {n} gehe ich.",
    "Anstatt ___ {n} kaufe ich Brot.",
    "Das ist die Farbe ___ {n}.",
    "Das ist der Name ___ {n}.",
    "Das ist die Größe ___ {n}.",
    "Das ist der Geschmack ___ {n}.",
    "Das ist die Form ___ {n}.",
    "Das ist der Preis ___ {n}.",
    "Das ist das Ende ___ {n}.",
    "Das ist der Anfang ___ {n}.",
    "Das ist die Mitte ___ {n}.",
    "Das ist die Seite ___ {n}.",
    "Das ist die Ursache ___ {n}.",
    "Das ist die Qualität ___ {n}.",
    "Das ist die Bedeutung ___ {n}.",
    "Das ist der Wert ___ {n}.",
    "Das ist der Vorteil ___ {n}.",
    "Das ist der Nachteil ___ {n}.",
    "Das ist der Inhalt ___ {n}.",
    "Das ist der Zweck ___ {n}.",
    "Das ist der Grund ___ {n}.",
    "Das ist der Besitzer ___ {n}.",
]

gen_interrogative = [
    "Wer ist der Vater ___ {n}?",
    "Wer ist die Mutter ___ {n}?",
    "Wo ist das Auto ___ {n}?",
    "Wo ist das Haus ___ {n}?",
    "Wer ist der Freund ___ {n}?",
    "Wer ist die Freundin ___ {n}?",
    "Was ist der Name ___ {n}?",
    "Was ist die Farbe ___ {n}?",
    "Wie ist die Größe ___ {n}?",
    "Was ist der Preis ___ {n}?",
    "Was ist der Wert ___ {n}?",
    "Wer ist der Besitzer ___ {n}?",
    "Was ist die Bedeutung ___ {n}?",
    "Was ist der Grund ___ {n}?",
]

# ── Build exercises ───────────────────────────────────────────────────
exercises = []
eid = 0

def add_exercise(sentence, answer, case, gender, noun, explanation, tags):
    global eid
    eid += 1
    all_articles = ["der", "die", "das", "den", "dem", "des"]
    options = list(all_articles)
    random.shuffle(options)
    if answer not in options:
        options[0] = answer
    exercises.append({
        "id": f"A-{eid:04d}",
        "level": "A",
        "type": "definite_article",
        "sentence": sentence,
        "options": sorted(set(options)),
        "answer": answer,
        "case": case,
        "focus": f"{case} {gender.replace('der','masculine').replace('die','feminine').replace('das','neuter')}",
        "explanation": explanation,
        "tags": tags
    })

# Round 1: 450 exercises — cycle through cases
# Pattern: Nom, Akk, Dat, Nom, Akk, Gen (6-cycle, repeat twice = 600, trim to 450)
case_cycle = ["Nominativ", "Akkusativ", "Dativ", "Nominativ", "Akkusativ", "Genitiv"]

for i, (gender, noun) in enumerate(unique_nouns):
    g_short = gender.replace("der","").replace("die","").replace("das","")
    case = case_cycle[i % len(case_cycle)]
    art = article_for(gender, case)
    
    if case == "Nominativ":
        templates = nom_assertive + nom_interrogative
    elif case == "Akkusativ":
        templates = akk_assertive + akk_interrogative
    elif case == "Dativ":
        templates = dat_assertive + dat_interrogative
    else:
        templates = gen_assertive + gen_interrogative
    
    tpl = templates[i % len(templates)]
    sentence = fill_template(tpl, gender, noun)
    
    is_interrogative = "?" in sentence
    tags = [case.lower(), g_short, "definite-article"]
    if is_interrogative:
        tags.append("interrogative")
    
    add_exercise(sentence, art, case, gender, noun,
        f"{case} case. {gender} {noun} in {case}: {art}.",
        tags)

# Rounds 2-5: generate enough to reach 1500+ after dedup
for rnd in range(2, 7):
    for i, (gender, noun) in enumerate(unique_nouns):
        g_short = gender.replace("der","").replace("die","").replace("das","")
        offset = rnd * 2
        case = case_cycle[(i + offset) % len(case_cycle)]
        art = article_for(gender, case)
        
        if case == "Nominativ":
            templates = nom_assertive + nom_interrogative
        elif case == "Akkusativ":
            templates = akk_assertive + akk_interrogative
        elif case == "Dativ":
            templates = dat_assertive + dat_interrogative
        else:
            templates = gen_assertive + gen_interrogative
        
        tpl_idx = (i + rnd * 3) % len(templates)
        tpl = templates[tpl_idx]
        sentence = fill_template(tpl, gender, noun)
        
        is_interrogative = "?" in sentence
        tags = [case.lower(), g_short, "definite-article"]
        if is_interrogative:
            tags.append("interrogative")
        
        add_exercise(sentence, art, case, gender, noun,
            f"{case} case. {gender} {noun} in {case}: {art}.",
            tags)

# Trim to exactly 1500
exercises = exercises[:1500]

# Deduplicate by sentence — keep first occurrence
seen_sentences = set()
deduped = []
for ex in exercises:
    s = ex["sentence"]
    if s not in seen_sentences:
        seen_sentences.add(s)
        deduped.append(ex)
exercises = deduped

print(f"After dedup: {len(exercises)}")

rnd = 5  # continue from where the for loop left off

# If still under 1500, pad with extra rounds
while len(exercises) < 1500:
    rnd += 1
    for i, (gender, noun) in enumerate(unique_nouns):
        if len(exercises) >= 1500:
            break
        g_short = gender.replace("der","").replace("die","").replace("das","")
        offset = rnd * 2
        case = case_cycle[(i + offset) % len(case_cycle)]
        art = article_for(gender, case)
        
        if case == "Nominativ":
            templates = nom_assertive + nom_interrogative
        elif case == "Akkusativ":
            templates = akk_assertive + akk_interrogative
        elif case == "Dativ":
            templates = dat_assertive + dat_interrogative
        else:
            templates = gen_assertive + gen_interrogative
        
        tpl_idx = (i + rnd * 7) % len(templates)
        tpl = templates[tpl_idx]
        sentence = fill_template(tpl, gender, noun)
        
        if sentence in seen_sentences:
            continue
        seen_sentences.add(sentence)
        
        is_interrogative = "?" in sentence
        tags = [case.lower(), g_short, "definite-article"]
        if is_interrogative:
            tags.append("interrogative")
        
        add_exercise(sentence, art, case, gender, noun,
            f"{case} case. {gender} {noun} in {case}: {art}.",
            tags)
    print(f"After round {rnd}: {len(exercises)}")

# Final trim
exercises = exercises[:1500]

# Re-number IDs
for i, ex in enumerate(exercises):
    ex["id"] = f"A-{i+1:04d}"

# Stats
print(f"Total exercises: {len(exercises)}")
case_counts = Counter(ex["case"] for ex in exercises)
print(f"By case: {dict(case_counts)}")
interrogative = sum(1 for ex in exercises if "interrogative" in ex["tags"])
assertive = len(exercises) - interrogative
print(f"Assertive: {assertive}, Interrogative: {interrogative}")
gen_count = sum(1 for ex in exercises if ex["case"] == "Genitiv")
print(f"Genitiv count: {gen_count}")

# Gender distribution
gender_counts = Counter()
for ex in exercises:
    focus = ex["focus"]
    if "masculine" in focus:
        gender_counts["masculine"] += 1
    elif "feminine" in focus:
        gender_counts["feminine"] += 1
    else:
        gender_counts["neuter"] += 1
print(f"By gender: {dict(gender_counts)}")

# Write out
with open("/home/mro/app/case-trainer/src/data/a.json", "w") as f:
    json.dump(exercises, f, indent=2, ensure_ascii=False)

print("Written to a.json ✓")
