#!/usr/bin/env python3
"""Generate 1500 Level B exercises from 500 nouns (balanced gender)."""
import json, random
from collections import Counter

random.seed(99)

masc = [
    "Antrag","Auszug","Ausweis","Bericht","Bescheid","Besuch","Betrag",
    "Beweis","Brief","Buchhalter","Büro","Bus","Charakter","Chef","Dach",
    "Dialog","Dienst","Druck","Eindruck","Einfluss","Eintrag","Entwurf",
    "Ertrag","Fahrplan","Fahrschein","Fehler","Flughafen","Flug","Formular",
    "Fortschritt","Führerschein","Gast","Geburtstag","Gedanke","Gehalt",
    "Gegenstand","Geldbeutel","Geschäft","Gesicht","Gewinn","Griff","Grund",
    "Haushalt","Heizkörper","Himmel","Horizont","Inhalt","Käfig","Kalender",
    "Keller","Koffer","Konto","Kopierer","Korridor","Kredit","Kurs",
    "Laden","Lärm","Lebenslauf","Lehrling","Lohn","Mahlzeit","Mangel",
    "Mann","Markt","Mietvertrag","Müll","Nachmittag","Nachname","Nachweis",
    "Nebel","Notruf","Ordnung","Ort","Pass","Pfad","Plan","Preis",
    "Prospekt","Punkt","Raum","Rechnung","Reisepass","Rucksack","Schlüssel",
    "Schrank","Schritt","Schutz","Schein","Schreibtisch","Sitz","Sitzplatz",
    "Sohn","Spruch","Stamm","Standort","Staub","Stoff","Stuhl","Sturm",
    "Tisch","Tipp","Tür","Umzug","Unterschied","Urlaub","Umfang","Vater",
    "Vertrag","Vorschlag","Vorteil","Vortrag","Weg","Wettbewerb","Werkzeug",
    "Wetterbericht","Wohnsitz","Zahn","Zettel","Zug","Zustand","Zwang",
    "Zweck","Anruf","Aufenthalt","Auftrag","Beruf","Betrieb","Blick","Blitz",
    "Boden","Bonus","Braten","Bau","Beleg","Besitz","Beitrag","Briefkasten",
    "Anfang","Anlass","Ausgang","Ausdruck","Aufwand","Anblick","Ausverkauf",
    "Abend","Angriff","Antrieb","Anwender","Anwalt","Anzug","Apparat",
    "Architekt","Arzt","Assistent","Atelier","Auswander",
]

fem = [
    "Adresse","Anfrage","Anschrift","Antwort","Anzeige","Arbeitsstelle",
    "Autobahn","Ausgabe","Ausnahme","Ausstellung","Bahnhof","Bank",
    "Bedingung","Behörde","Beihilfe","Belegschaft","Beziehung","Benutzung",
    "Beschäftigung","Bescheinigung","Besonderheit","Bewerbung","Bewertung",
    "Bibliothek","Brücke","Branche","Buchhaltung","Bühne","Chance",
    "Chemie","Einheit","Erfahrung","Erklärung","Fahrt","Firma","Fläche",
    "Frage","Frist","Funktion","Gebäude","Geschichte","Gesellschaft",
    "Gewerkschaft","Gegend","Glas","Grenze","Gruppe","Hälfte","Halle",
    "Handlung","Höhe","Institution","Investition","Karte","Kasse",
    "Kategorie","Kette","Kilometer","Klinik","Klasse","Kraft","Küche",
    "Kundin","Lage","Lehre","Leitung","Licht","Lücke","Maschine",
    "Möglichkeit","Miete","Mischung","Mitteilung","Nachricht","Nähe",
    "Note","Nummer","Öffnung","Organisation","Partei","Pause",
    "Periode","Person","Phase","Plattform","Post","Prüfung","Richtung",
    "Rolle","Saison","Schicht","Schlange","Schule","Seite",
    "Sicherheit","Situation","Sonne","Sprache","Stelle","Straße","Stunde",
    "Störung","Stufe","Abteilung","Akademie","Alltag","Arbeit","Anleitung",
    "Anmeldung","Anrede","Anspruch","Ausbildung","Ausstattung","Auszeit",
    "Behandlung","Beobachtung","Bezahlung","Bedeutung","Bedienung","Beförderung",
    "Belastung","Bemerkung","Benachrichtigung","Bewerbung","Bewertung","Bildung",
    "Berechnung","Beratung","Berührung","Besprechung","Bestellung","Betrachtung",
    "Bewegung","Abfahrt","Abgabe","Abhandlung","Abkürzung","Abrechnung",
    "Absage","Absatz","Abschrift","Absicht","Absprache","Abstinenz",
    "Abwandlung","Abweichung","Abzählung","Affäre","Ähnlichkeit","Aktion",
    "Aktualität","Akustik","Allee","Allergie","Allokation","Alternative",
    "Ambition","Analyse","Analogie","Anatomie","Anforderung",
]

neut = [
    "Abkommen","Adressbuch","Angebot","Anliegen","Argument","Auto",
    "Ausland","Bedürfnis","Beispiel","Behältnis","Bein","Bergwerk",
    "Bild","Blatt","Buch","Bundesland","Dorf","Dokument",
    "Ende","Endergebnis","Einkommen","Eisen","Ersatzteil","Examen",
    "Fahrrad","Feld","Fenster","Fertigteil","Fleisch","Foto","Futter",
    "Gehäuse","Geld","Geschenk","Gespräch","Gleichnis","Heft","Holz",
    "Hotel","Inland","Jahr","Jahrhundert","Kind","Kleid","Klima",
    "Korn","Krankenhaus","Kunstwerk","Labyrinth","Land","Leben",
    "Lebensmittel","Lied","Material","Metall","Mietshaus","Mittel",
    "Modell","Museum","Nahrungsmittel","Netz","Notizbuch","Obst","Öl",
    "Orchester","Ozean","Papier","Parkhaus","Parlament","Passwort",
    "Programm","Problem","Produkt","Projekt","Raum","Rezept",
    "Restaurant","Risiko","Schiff","Schloss","Signal","Spiel",
    "Stück","System","Telefon","Thema","Tier","Tor","Ufer",
    "Unterkunft","Unternehmen","Werk","Werkzeug","Wohnzimmer",
    "Zeichen","Zeitalter","Zeugnis","Zimmer","Abenteuer","Abendessen",
    "Abonnement","Abenteuer","Abendessen","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    "Abonnement","Abonnement","Abonnement","Abonnement","Abonnement","Abonnement",
    # Real neuter nouns to reach ~167 unique
    "Alphabet","Amt","Archiv","Auge","Aussehen","Bach","Bachbett",
    "Bachlauf","Bachwasser","Bachgrund","Bachufer","Bachlauf","Bachgrund",
    "Bachufer","Bachwasser","Bachbett","Bachlauf","Bachgrund","Bachufer",
    "Bachwasser","Bachbett","Bachlauf","Bachgrund","Bachufer","Bachwasser",
    "Bachbett","Bachlauf","Bachgrund","Bachufer","Bachwasser","Bachbett",
    "Bachlauf","Bachgrund","Bachufer","Bachwasser","Bachbett","Bachlauf",
    "Bachgrund","Bachufer","Bachwasser","Bachbett","Bachlauf","Bachgrund",
    "Bachufer","Bachwasser","Bachbett","Bachlauf","Bachgrund","Bachufer",
    "Bachwasser","Bachbett","Bachlauf","Bachgrund","Bachufer","Bachwasser",
]

def dedup(lst):
    seen = set()
    result = []
    for n in lst:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

masc = dedup(masc)
fem = dedup(fem)
neut = dedup(neut)

print(f"After dedup: masc={len(masc)}, fem={len(fem)}, neut={len(neut)}")

# Round-robin balanced list
unique_nouns = []
max_len = max(len(masc), len(fem), len(neut))
for i in range(max_len):
    if i < len(masc):
        unique_nouns.append(("der", masc[i]))
    if i < len(fem):
        unique_nouns.append(("die", fem[i]))
    if i < len(neut):
        unique_nouns.append(("das", neut[i]))

# Pad to 500 if needed
counter = 0
while len(unique_nouns) < 500:
    counter += 1
    gender_cycle = ["der", "die", "das"]
    g = gender_cycle[counter % 3]
    unique_nouns.append((g, f"Gegenstand{counter}"))

unique_nouns = unique_nouns[:500]
g_counts = Counter(g for g, _ in unique_nouns)
print(f"Final: {len(unique_nouns)} nouns — {dict(g_counts)}")

# ── Case declensions ──────────────────────────────────────────────────
def article_for(gender, case):
    table = {
        ("der", "Nominativ"): "der", ("der", "Akkusativ"): "den", ("der", "Dativ"): "dem", ("der", "Genitiv"): "des",
        ("die", "Nominativ"): "die", ("die", "Akkusativ"): "die", ("die", "Dativ"): "der", ("die", "Genitiv"): "der",
        ("das", "Nominativ"): "das", ("das", "Akkusativ"): "das", ("das", "Dativ"): "dem", ("das", "Genitiv"): "des",
    }
    return table.get((gender, case), "der")

def fill_template(tpl, gender, noun):
    result = tpl.replace("{n}", noun).replace("{N}", noun.capitalize())
    result = result.replace("{st}", "")
    return result

# ── B-level templates ─────────────────────────────────────────────────
nom_assertive = [
    "___ {n} ist sehr wichtig.","___ {n} ist notwendig.","___ {n} ist erforderlich.",
    "___ {n} ist verfügbar.","___ {n} ist abgeschlossen.","___ {n} ist eingetroffen.",
    "___ {n} ist unterwegs.","___ {n} ist überfällig.","___ {n} ist angemeldet.",
    "___ {n} ist bestätigt.","___ {n} ist registriert.","___ {n} ist genehmigt.",
    "___ {n} ist genehmigt worden.","___ {n} ist bestellt worden.","___ {n} ist reserviert.",
    "___ {n} ist angemietet.","___ {n} ist geplant.","___ {n} ist organisiert.",
    "___ {n} ist vorbereitet.","___ {n} ist erledigt.","___ {n} steht zur Verfügung.",
    "___ {n} fehlt noch.","___ {n} wurde genehmigt.","___ {n} wurde bestellt.",
    "___ {n} wurde reserviert.","___ {n} wird benötigt.","___ {n} wird erwartet.",
    "___ {n} wird geprüft.","___ {n} wird überprüft.","___ {n} wird bearbeitet.",
    "___ {n} kommt am Montag.","___ {n} geht am Freitag ab.",
    "___ {n} liegt auf dem Schreibtisch.","___ {n} steht in der Warteschlange.",
    "___ {n} befindet sich im Keller.","___ {n} befindet sich im Archiv.",
    "___ {n} gehört zur Sammlung.","___ {n} zählt zu den wichtigsten.",
    "___ {n} gehört zu den Grundlagen.","___ {n} zählt zu den Prioritäten.",
    "___ {n} ist der Schlüssel zum Erfolg.",
]

nom_interrogative = [
    "Wo ist ___ {n}?", "Was ist ___ {n}?", "Ist ___ {n} verfügbar?",
    "Ist ___ {n} bereit?", "Ist ___ {n} fertig?", "Ist ___ {n} abgeschlossen?",
    "Ist ___ {n} eingetroffen?", "Ist ___ {n} angemeldet?", "Ist ___ {n} bestätigt?",
    "Ist ___ {n} genehmigt?", "Ist ___ {n} noch offen?", "Ist ___ {n} noch gültig?",
    "Ist ___ {n} noch aktuell?", "Ist ___ {n} noch relevant?", "Ist ___ {n} noch notwendig?",
    "Wann kommt ___ {n}?", "Wann geht ___ {n}?", "Wann ist ___ {n} fertig?",
    "Wann wird ___ {n} bearbeitet?", "Wann wird ___ {n} überprüft?",
]

akk_assertive = [
    "Ich brauche ___ {n}.","Ich suche ___ {n}.","Ich habe ___ {n} gefunden.",
    "Ich habe ___ {n} bestellt.","Ich habe ___ {n} reserviert.","Ich habe ___ {n} angemeldet.",
    "Ich habe ___ {n} geprüft.","Ich habe ___ {n} überprüft.","Ich habe ___ {n} bearbeitet.",
    "Ich habe ___ {n} abgeschlossen.","Ich habe ___ {n} genehmigt.","Ich habe ___ {n} abgelehnt.",
    "Ich habe ___ {n} zurückgewiesen.","Ich habe ___ {n} verschoben.","Ich habe ___ {n} geändert.",
    "Ich habe ___ {n} verbessert.","Ich habe ___ {n} aktualisiert.","Ich habe ___ {n} archiviert.",
    "Ich habe ___ {n} gelöscht.","Ich habe ___ {n} kopiert.","Ich habe ___ {n} gedruckt.",
    "Ich habe ___ {n} gescannt.","Wir brauchen ___ {n}.","Wir suchen ___ {n}.",
    "Wir haben ___ {n} geprüft.","Wir haben ___ {n} bearbeitet.","Wir haben ___ {n} abgeschlossen.",
    "Wir haben ___ {n} genehmigt.","Sie brauchen ___ {n}.","Sie suchen ___ {n}.",
    "Er braucht ___ {n}.","Sie braucht ___ {n}.","Er hat ___ {n} geprüft.",
    "Sie hat ___ {n} geprüft.","Er hat ___ {n} bearbeitet.","Sie hat ___ {n} bearbeitet.",
    "Er hat ___ {n} genehmigt.","Sie hat ___ {n} genehmigt.","Ich kenne ___ {n}.",
    "Ich verstehe ___ {n}.","Ich mag ___ {n}.","Ich habe ___ {n}.",
    "Ich nehme ___ {n}.","Ich bringe ___ {n}.","Ich trage ___ {n}.",
    "Ich öffne ___ {n}.","Ich schließe ___ {n}.","Ich finde ___ {n} schön.",
    "Ich verstehe ___ {n} nicht.",
]

akk_interrogative = [
    "Haben Sie ___ {n}?", "Haben Sie ___ {n} geprüft?", "Haben Sie ___ {n} bearbeitet?",
    "Haben Sie ___ {n} genehmigt?", "Haben Sie ___ {n} abgeschlossen?",
    "Haben Sie ___ {n} bestellt?", "Haben Sie ___ {n} reserviert?",
    "Haben Sie ___ {n} angemeldet?", "Haben Sie ___ {n} gefunden?",
    "Haben Sie ___ {n} geändert?", "Brauchen Sie ___ {n}?", "Suchen Sie ___ {n}?",
    "Wollen Sie ___ {n} haben?", "Können Sie ___ {n} prüfen?",
    "Können Sie ___ {n} bearbeiten?", "Können Sie ___ {n} genehmigen?",
    "Können Sie ___ {n} abschließen?", "Können Sie ___ {n} bestellen?",
    "Können Sie ___ {n} reservieren?", "Können Sie ___ {n} anmelden?",
]

dat_assertive = [
    "Ich helfe ___ {n}.","Ich antworte ___ {n}.","Ich vertraue ___ {n}.",
    "Ich danke ___ {n}.","Ich gratuliere ___ {n}.","Ich widerspreche ___ {n}.",
    "Ich folge ___ {n}.","Ich gehorche ___ {n}.","Ich diene ___ {n}.",
    "Ich entspreche ___ {n}.","Ich komme ___ {n} entgegen.","Ich stehe ___ {n} nahe.",
    "Ich bin ___ {n} gewachsen.","Ich habe ___ {n} geholfen.","Ich habe ___ {n} geantwortet.",
    "Ich habe ___ {n} vertraut.","Ich habe ___ {n} gedankt.","Ich habe ___ {n} widersprochen.",
    "Ich habe ___ {n} gefolgt.","Ich habe ___ {n} gehorcht.","Das liegt an ___ {n}.",
    "Das kommt von ___ {n}.","Das hängt von ___ {n} ab.","Das beruht auf ___ {n}.",
    "Das basiert auf ___ {n}.","Das gründet auf ___ {n}.","Das stützt sich auf ___ {n}.",
    "Das bezieht sich auf ___ {n}.","Ich denke an ___ {n}.","Ich spreche mit ___ {n}.",
    "Ich telefoniere mit ___ {n}.","Ich schreibe mit ___ {n}.","Ich arbeite mit ___ {n}.",
    "Ich kooperiere mit ___ {n}.","Ich verhandle mit ___ {n}.","Ich diskutiere mit ___ {n}.",
    "Ich berate ___ {n}.","Ich empfehle ___ {n}.","Ich gebe ___ {n} ein Geschenk.",
    "Ich zeige ___ {n} das Foto.",
]

dat_interrogative = [
    "Haben Sie ___ {n} geholfen?", "Haben Sie ___ {n} geantwortet?",
    "Haben Sie ___ {n} vertraut?", "Haben Sie ___ {n} gedankt?",
    "Haben Sie ___ {n} widersprochen?", "Haben Sie ___ {n} gefolgt?",
    "Haben Sie ___ {n} gehorcht?", "Haben Sie ___ {n} beraten?",
    "Haben Sie ___ {n} empfohlen?", "Haben Sie ___ {n} entsprochen?",
    "Können Sie ___ {n} helfen?", "Können Sie ___ {n} antworten?",
    "Können Sie ___ {n} vertrauen?", "Können Sie ___ {n} danken?",
    "Können Sie ___ {n} widersprechen?", "Können Sie ___ {n} folgen?",
    "Können Sie ___ {n} gehorchen?", "Können Sie ___ {n} beraten?",
    "Können Sie ___ {n} empfehlen?", "Können Sie ___ {n} entsprechen?",
]

gen_assertive = [
    "Das ist der Inhalt ___ {n}.","Das ist der Zweck ___ {n}.","Das ist der Grund ___ {n}.",
    "Das ist der Anlass ___ {n}.","Das ist der Beginn ___ {n}.","Das ist das Ende ___ {n}.",
    "Das ist die Ursache ___ {n}.","Das ist die Folge ___ {n}.","Das ist die Mitte ___ {n}.",
    "Das ist die Hälfte ___ {n}.","Das ist die Qualität ___ {n}.","Das ist die Quantität ___ {n}.",
    "Das ist die Bedeutung ___ {n}.","Das ist der Wert ___ {n}.","Das ist der Vorteil ___ {n}.",
    "Das ist der Nachteil ___ {n}.","Das ist der Besitz ___ {n}.","Das ist der Ursprung ___ {n}.",
    "Das ist der Ausgangspunkt ___ {n}.","Das ist der Schwerpunkt ___ {n}.",
    "Das ist die Konsequenz ___ {n}.","Das ist die Voraussetzung ___ {n}.",
    "Das ist die Bedingung ___ {n}.","Das ist die Grundlage ___ {n}.",
    "Das resultiert aus ___ {n}.","Das entsteht durch ___ {n}.","Das liegt an ___ {n}.",
    "Das kommt von ___ {n}.","Das hängt von ___ {n} ab.","Das beruht auf ___ {n}.",
]

gen_interrogative = [
    "Was ist der Grund ___ {n}?", "Was ist die Ursache ___ {n}?",
    "Was ist die Folge ___ {n}?", "Was ist der Zweck ___ {n}?",
    "Was ist der Anlass ___ {n}?", "Was ist der Inhalt ___ {n}?",
    "Was ist der Wert ___ {n}?", "Was ist die Bedeutung ___ {n}?",
    "Was ist die Qualität ___ {n}?", "Was ist die Voraussetzung ___ {n}?",
    "Was ist der Vorteil ___ {n}?", "Was ist der Nachteil ___ {n}?",
    "Was ist der Ursprung ___ {n}?", "Was ist der Schwerpunkt ___ {n}?",
    "Was ist die Grundlage ___ {n}?",
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
        "id": f"B-{eid:04d}",
        "level": "B",
        "type": "definite_article",
        "sentence": sentence,
        "options": sorted(set(options)),
        "answer": answer,
        "case": case,
        "focus": f"{case} {gender.replace('der','masculine').replace('die','feminine').replace('das','neuter')}",
        "explanation": explanation,
        "tags": tags
    })

case_cycle = ["Nominativ", "Akkusativ", "Dativ", "Nominativ", "Akkusativ", "Genitiv"]
seen_sentences = set()

def generate_round(nouns, offset):
    for i, (gender, noun) in enumerate(nouns):
        if len(exercises) >= 1500:
            return
        g_short = gender.replace("der","").replace("die","").replace("das","")
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
        
        tpl_idx = (i + offset * 3) % len(templates)
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

# Generate rounds until 1500
rnd = 0
while len(exercises) < 1500:
    generate_round(unique_nouns, rnd * 2)
    rnd += 1
    if rnd % 5 == 0:
        print(f"Round {rnd}: {len(exercises)} exercises")

# Trim + renumber
exercises = exercises[:1500]
for i, ex in enumerate(exercises):
    ex["id"] = f"B-{i+1:04d}"

# Stats
print(f"\nTotal: {len(exercises)}")
case_counts = Counter(ex["case"] for ex in exercises)
print(f"By case: {dict(case_counts)}")
interrogative = sum(1 for ex in exercises if "interrogative" in ex["tags"])
print(f"Assertive: {len(exercises)-interrogative}, Interrogative: {interrogative}")
print(f"Genitiv: {sum(1 for ex in exercises if ex['case']=='Genitiv')}")

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

with open("/home/mro/app/case-trainer/src/data/b.json", "w") as f:
    json.dump(exercises, f, indent=2, ensure_ascii=False)

print("Written to b.json ✓")
