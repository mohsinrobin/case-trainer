"""Level A data: everyday vocabulary (roughly A1 + A2).

NOUNS   Noun|gender(m/f/n/p)|plural|genitive ending|tags
        genitive ending: es / s / ses  (m, n)   - (f, p)   W:n / W:en (weak noun: Akk/Dat/Gen get -n/-en)
        plural "-" = no plural (mass noun).  gender p = plural-only noun.
FRAMES  KIND|key|tags|genders|sentence   ({N} = blank + noun, <sg|pl> = verb agreement)
        kinds: NS subject, NP predicate noun, AV verb+Akk, AP prep+Akk, AW two-way prep (movement) +Akk,
               DV verb+Dat, DI indirect object, DP prep+Dat, DW two-way prep (position) +Dat,
               GP prep+Gen, GA genitive attribute
        A frame is only combined with nouns that have at least one of its tags.
        genders: * = all, otherwise letters (e.g. fp). Contracting prepositions (in, an, bei, von, zu) are only
        used where no contraction (im, am, beim, vom, zum) would be natural.
"""

NOUNS = """
# ---- people
Mann|m|Männer|es|person adult
Frau|f|Frauen|-|person adult
Kind|n|Kinder|es|person child family
Baby|n|Babys|s|person baby family
Mädchen|n|Mädchen|s|person child
Junge|m|Jungen|W:n|person child
Vater|m|Väter|s|person adult family
Mutter|f|Mütter|-|person adult family host
Bruder|m|Brüder|s|person adult family
Schwester|f|Schwestern|-|person adult family host
Sohn|m|Söhne|es|person adult child family
Tochter|f|Töchter|-|person adult child family
Eltern|p|Eltern|-|person adult family parents
Großeltern|p|Großeltern|-|person adult family parents
Großvater|m|Großväter|s|person adult family
Großmutter|f|Großmütter|-|person adult family host
Onkel|m|Onkel|s|person adult family
Tante|f|Tanten|-|person adult family host
Freund|m|Freunde|es|person adult friend
Freundin|f|Freundinnen|-|person adult friend host
Nachbar|m|Nachbarn|W:n|person adult
Nachbarin|f|Nachbarinnen|-|person adult
Kollege|m|Kollegen|W:n|person adult job
Kollegin|f|Kolleginnen|-|person adult job
Student|m|Studenten|W:en|person adult
Studentin|f|Studentinnen|-|person adult
Lehrer|m|Lehrer|s|person adult job
Lehrerin|f|Lehrerinnen|-|person adult job
Arzt|m|Ärzte|es|person adult job
Ärztin|f|Ärztinnen|-|person adult job
Kellner|m|Kellner|s|person adult job
Kellnerin|f|Kellnerinnen|-|person adult job
Koch|m|Köche|s|person adult job
Köchin|f|Köchinnen|-|person adult job
Fahrer|m|Fahrer|s|person adult job
Verkäufer|m|Verkäufer|s|person adult job
Verkäuferin|f|Verkäuferinnen|-|person adult job
Chef|m|Chefs|s|person adult job
Chefin|f|Chefinnen|-|person adult job
Polizist|m|Polizisten|W:en|person adult job
Bäcker|m|Bäcker|s|person adult job
Gast|m|Gäste|es|person adult
Herr|m|Herren|W:n|person adult
Kunde|m|Kunden|W:n|person adult
Kundin|f|Kundinnen|-|person adult
Mensch|m|Menschen|W:en|person adult
Klasse|f|Klassen|-|group loud
# ---- animals
Hund|m|Hunde|es|animal pet loud
Katze|f|Katzen|-|animal pet
Kaninchen|n|Kaninchen|s|animal pet
Vogel|m|Vögel|s|animal
Fisch|m|Fische|es|animal food cook
Pferd|n|Pferde|es|animal
Kuh|f|Kühe|-|animal
Maus|f|Mäuse|-|animal
Tier|n|Tiere|es|animal
Affe|m|Affen|W:n|animal
# ---- food and drink
Brot|n|Brote|es|food bake swap
Brötchen|n|Brötchen|s|food bake
Käse|m|-|s|food spread
Kuchen|m|Kuchen|s|food bake swap
Apfel|m|Äpfel|s|food
Banane|f|Bananen|-|food
Birne|f|Birnen|-|food
Orange|f|Orangen|-|food
Tomate|f|Tomaten|-|food spread
Kartoffel|f|Kartoffeln|-|food cook
Salat|m|Salate|s|food spread
Suppe|f|-|-|food cook swap
Ei|n|Eier|es|food cook spread
Eis|n|-|es|food
Fleisch|n|-|es|food cook spread swap
Reis|m|-|es|food cook
Nudeln|p|Nudeln|-|food cook
Wurst|f|-|-|food cook spread swap
Schokolade|f|-|-|food spread
Butter|f|-|-|food spread
Marmelade|f|-|-|food spread
Zucker|m|-|s|mix
Honig|m|-|s|mix
Zitrone|f|Zitronen|-|mix
Frühstück|n|-|s|meal
Mittagessen|n|-|s|meal after
Abendessen|n|-|s|meal after
Essen|n|-|s|meal
Kaffee|m|-|s|drink swap
Tee|m|Tees|s|drink
Saft|m|Säfte|s|drink swap
Wasser|n|-|s|drink
Milch|f|-|-|drink mix swap
Bier|n|Biere|es|drink swap
Wein|m|Weine|es|drink swap
Limonade|f|Limonaden|-|drink
# ---- things
Schlüssel|m|Schlüssel|s|thing obj
Handy|n|Handys|s|thing obj device pack repair gift
Tasche|f|Taschen|-|thing obj pack close open container
Brille|f|Brillen|-|thing obj
Geldbeutel|m|Geldbeutel|s|thing obj
Regenschirm|m|Regenschirme|es|thing obj pack
Uhr|f|Uhren|-|thing obj repair gift
Ball|m|Bälle|s|thing obj gift
Koffer|m|Koffer|s|thing obj pack close open container
Rucksack|m|Rucksäcke|s|thing obj pack close open container
Flasche|f|Flaschen|-|thing obj close open
Glas|n|Gläser|es|thing obj wash
Tasse|f|Tassen|-|thing obj wash
Teller|m|Teller|s|thing obj wash
Messer|n|Messer|s|thing obj wash
Gabel|f|Gabeln|-|thing obj wash
Löffel|m|Löffel|s|thing obj wash
Geschenk|n|Geschenke|es|thing obj receive open
Kamera|f|Kameras|-|thing obj device pack gift
Computer|m|Computer|s|obj device repair
Fernseher|m|Fernseher|s|obj device repair loud
Radio|n|-|s|obj device listen repair loud
Drucker|m|Drucker|s|obj device repair loud
Ticket|n|Tickets|s|thing obj receive reserve gift
Karte|f|Karten|-|thing obj receive reserve gift
Geld|n|-|es|thing
Lampe|f|Lampen|-|furniture obj device repair
# ---- media
Buch|n|Bücher|es|media obj text write gift close open story readable title pack paper
Zeitung|f|Zeitungen|-|media obj text readable receive title paper
Zeitschrift|f|Zeitschriften|-|media obj text readable title paper
Film|m|Filme|s|media watch story title after show
Lied|n|Lieder|es|media listen story title
Bild|n|Bilder|es|media obj watch paint gift paper
Foto|n|Fotos|s|media obj watch gift paper
Brief|m|Briefe|es|media obj text write receive answer readable open paper
E-Mail|f|E-Mails|-|media text write answer
Nachricht|f|Nachrichten|-|media text write answer
# ---- clothes
Jacke|f|Jacken|-|clothes obj wash hang pack
Hose|f|Hosen|-|clothes obj wash hang pack
Kleid|n|Kleider|es|clothes obj wash hang gift pack
Mantel|m|Mäntel|s|clothes obj wash hang pack
Schuh|m|Schuhe|es|shoe
Hut|m|Hüte|es|clothes obj gift pack
Mütze|f|Mützen|-|clothes obj wash gift pack
Schal|m|Schals|s|clothes obj wash hang gift pack
Pullover|m|Pullover|s|clothes obj wash gift pack
Hemd|n|Hemden|es|clothes obj wash hang pack
# ---- furniture and home
Tisch|m|Tische|es|furniture obj surface under over free reserve hit repair clean coverable
Stuhl|m|Stühle|es|furniture obj surface under seat free repair coverable
Bett|n|Betten|es|furniture obj surface under seat over free hideplace coverable
Sofa|n|Sofas|s|furniture obj surface under seat over hideplace coverable
Schrank|m|Schränke|es|furniture obj surface over hideplace wall clean hit container coverable
Regal|n|Regale|s|furniture obj surface hideplace coverable
Teppich|m|Teppiche|s|obj surface seat
Spiegel|m|Spiegel|s|furniture obj over clean hit
Tür|f|Türen|-|part wall over hideplace open close repair hit
Fenster|n|Fenster|s|part open close repair clean hit
Wand|f|Wände|-|part wall hit
Dach|n|Dächer|es|part
# ---- vehicles
Auto|n|Autos|s|vehicle obj ride parked hit wash repair
Bus|m|Busse|ses|vehicle transit ride parked miss
Zug|m|Züge|es|vehicle transit ride miss
Fahrrad|n|Fahrräder|es|vehicle obj ride parked repair
Flugzeug|n|Flugzeuge|s|vehicle miss
Taxi|n|Taxis|s|vehicle ride parked
Schiff|n|Schiffe|es|vehicle
Motorrad|n|Motorräder|es|vehicle obj ride parked repair
U-Bahn|f|U-Bahnen|-|vehicle transit ride miss
Straßenbahn|f|Straßenbahnen|-|vehicle transit ride miss
# ---- places and rooms
Stadt|f|Städte|-|place go through around scene sight visit come_from settle live
Dorf|n|Dörfer|es|place through around scene sight visit come_from settle
Park|m|Parks|s|place go through around scene visit
Garten|m|Gärten|s|place go around
Bahnhof|m|Bahnhöfe|es|place building go come_from
Flughafen|m|Flughäfen|s|place building come_from
Supermarkt|m|Supermärkte|s|place building shop go come_from institution
Bäckerei|f|Bäckereien|-|place building shop go come_from work
Apotheke|f|Apotheken|-|place building shop go come_from work
Kino|n|Kinos|s|place building shop come_from visit
Schule|f|Schulen|-|place building go come_from work sight institution grounds
Bibliothek|f|Bibliotheken|-|place building shop go come_from work institution
Restaurant|n|Restaurants|s|place building shop come_from visit institution grounds
Café|n|Cafés|s|place building shop come_from visit grounds
Schwimmbad|n|Schwimmbäder|es|place building shop come_from visit
Hotel|n|Hotels|s|place building come_from sight institution grounds
Museum|n|Museen|s|place building shop come_from visit sight institution grounds
Krankenhaus|n|Krankenhäuser|es|place building come_from institution grounds
Bank|f|Banken|-|place building shop go work come_from institution
Kirche|f|Kirchen|-|place building go visit sight grounds
Markt|m|Märkte|es|place shop go visit
Strand|m|Strände|es|place visit
Berg|m|Berge|es|place scene
Wald|m|Wälder|es|place go through scene
Fluss|m|Flüsse|es|place scene
Straße|f|Straßen|-|place through live loud
Platz|m|Plätze|es|place free reserve
Brücke|f|Brücken|-|place scene
Haus|n|Häuser|es|building sight come_from hit around hideplace grounds
Wohnung|f|Wohnungen|-|building live come_from free grounds
Büro|n|Büros|s|room building come_from
Küche|f|Küchen|-|room go clean work come_from
Bad|n|Bäder|es|room clean come_from
Wohnzimmer|n|Wohnzimmer|s|room clean
Schlafzimmer|n|Schlafzimmer|s|room clean
Zimmer|n|Zimmer|s|room clean free reserve come_from
Flur|m|Flure|s|room go clean come_from
Keller|m|Keller|s|room go clean come_from
Balkon|m|Balkone|s|room go clean
Haltestelle|f|Haltestellen|-|place wait_at
Kasse|f|Kassen|-|place wait_at
Ampel|f|Ampeln|-|place wait_at
Weg|m|Wege|es|place askabout
# ---- body
Kopf|m|Köpfe|es|body
Arm|m|Arme|es|body break
Bein|n|Beine|es|body break
Fuß|m|Füße|es|body break
Hand|f|Hände|-|body break point
Finger|m|Finger|s|body break point
Auge|n|Augen|s|body
Ohr|n|Ohren|es|body
Nase|f|Nasen|-|body break
Mund|m|Münder|es|body
Zahn|m|Zähne|es|body
Rücken|m|Rücken|s|body
Bauch|m|Bäuche|es|body
Hals|m|Hälse|es|body
# ---- time and events
Tag|m|Tage|es|time nice period within
Morgen|m|Morgen|s|time nice
Abend|m|Abende|s|time nice
Nacht|f|Nächte|-|time period
Woche|f|Wochen|-|time period within
Wochenende|n|Wochenenden|s|time nice trip plan period
Monat|m|Monate|s|time period within
Jahr|n|Jahre|es|time period within
Geburtstag|m|Geburtstage|s|time nice since
Urlaub|m|Urlaube|s|event nice trip plan since story period after
Ferien|p|Ferien|-|event nice trip plan since story period after
Konzert|n|Konzerte|es|event nice organize story since after show
Party|f|Partys|-|event nice organize plan since after
Fest|n|Feste|es|event nice organize plan since after
Termin|m|Termine|s|event free
Unterricht|m|-|s|event story after show
Test|m|Tests|s|event do since after show
Prüfung|f|Prüfungen|-|event do since after show
Kurs|m|Kurse|es|event story since after show
Reise|f|Reisen|-|event nice trip do plan organize since after
Besuch|m|Besuche|es|event plan
Arbeit|f|-|-|event after abstract
# ---- weather, causes
Regen|m|-|s|weather badweather cause lasting
Schnee|m|-|s|weather badweather cause lasting
Wind|m|-|es|weather badweather cause lasting
Sturm|m|-|es|weather badweather cause loud lasting
Sonne|f|-|-|weather
Hitze|f|-|-|weather badweather cause lasting
Kälte|f|-|-|weather badweather cause lasting
Nebel|m|-|s|weather badweather cause lasting
Stau|m|-|s|cause
Krankheit|f|-|-|cause
Lärm|m|-|s|cause
Verspätung|f|Verspätungen|-|cause
Streik|m|-|s|cause
# ---- plants and misc
Baum|m|Bäume|es|plant under hit paint
Blume|f|Blumen|-|plant thing gift paint
Rose|f|Rosen|-|plant gift paint
Pflanze|f|Pflanzen|-|plant
Sport|m|-|s|sport
Fußball|m|-|s|sport
Idee|f|Ideen|-|abstract
Frage|f|Fragen|-|abstract answer
Antwort|f|Antworten|-|abstract
Aufgabe|f|Aufgaben|-|abstract do
Hausaufgabe|f|Hausaufgaben|-|abstract do
Wort|n|Wörter|es|abstract
Problem|n|Probleme|s|abstract
Spiel|n|Spiele|es|watch story
"""

FRAMES = """
# ================= NOMINATIV =================
NS|kommen|person|*|{N} <kommt|kommen> heute etwas später.
NS|arbeiten|job|*|{N} <arbeitet|arbeiten> jeden Tag bis fünf Uhr.
NS|wohnen|adult|*|{N} <wohnt|wohnen> seit drei Jahren in Hamburg.
NS|lachen|person|*|{N} <lacht|lachen> laut über den Witz.
NS|warten|adult|*|{N} <wartet|warten> schon eine halbe Stunde vor dem Kino.
NS|sprechen|adult|*|{N} <spricht|sprechen> sehr schnell.
NS|schlafen|person|*|{N} <schläft|schlafen> noch, es ist erst sechs Uhr.
NS|singen|adult|*|{N} <singt|singen> gern unter der Dusche.
NS|essen|person|*|{N} <isst|essen> gern Nudeln zum Mittagessen.
NS|lernen|adult|*|{N} <lernt|lernen> jeden Abend Deutsch.
NS|fahren|adult|*|{N} <fährt|fahren> jeden Morgen mit dem Bus zur Arbeit.
NS|bleiben|person|*|{N} <bleibt|bleiben> heute zu Hause.
NS|lesen|adult|*|{N} <liest|lesen> im Bus die Zeitung.
NS|spielen|child|*|{N} <spielt|spielen> im Garten Fußball.
NS|weinen|child|*|{N} <weint|weinen> laut im Auto.
NS|weinen|baby|*|{N} <weint|weinen> laut im Auto.
NS|kochen|adult|*|{N} <kocht|kochen> heute Abend für alle.
NS|schwimmen|adult|*|{N} <schwimmt|schwimmen> jeden Sonntag im See.
NS|einkaufen|adult|*|{N} <kauft|kaufen> jeden Samstag auf dem Markt ein.
NS|schlafen|pet|*|{N} <schläft|schlafen> den ganzen Tag auf dem Sofa.
NS|fressen|animal|*|{N} <frisst|fressen> jeden Tag zweimal.
NS|brauchen|animal|*|{N} <braucht|brauchen> viel Platz und gutes Futter.
NS|haben|animal|*|{N} <hat|haben> großen Hunger.
NS|liegen|thing|*|{N} <liegt|liegen> schon seit gestern auf dem Tisch.
NS|liegen|paper|*|{N} <liegt|liegen> noch auf dem Tisch.
NS|fallen|thing|*|{N} <fällt|fallen> gleich vom Tisch.
NS|stehen|furniture|*|{N} <steht|stehen> im Wohnzimmer.
NS|kosten|obj|*|{N} <kostet|kosten> gar nicht so viel.
NS|sein|obj|*|{N} <ist|sind> leider kaputt.
NS|sein|furniture|*|{N} <ist|sind> ganz neu und nicht billig.
NS|sein|device|*|{N} <ist|sind> ganz neu und nicht billig.
NS|sein|vehicle|*|{N} <ist|sind> ganz neu und nicht billig.
NS|funktionieren|device|*|{N} <funktioniert|funktionieren> nicht mehr.
NS|fahren|transit|*|{N} <fährt|fahren> alle zehn Minuten.
NS|kommen|transit|*|{N} <kommt|kommen> heute leider zu spät.
NS|stehen|parked|*|{N} <steht|stehen> vor dem Haus.
NS|schmecken|food|*|{N} <schmeckt|schmecken> wirklich gut.
NS|schmecken|drink|*|{N} <schmeckt|schmecken> wirklich gut.
NS|sein|food|*|{N} <ist|sind> heute im Angebot.
NS|sein|drink|*|{N} <ist|sind> heute im Angebot.
NS|stehen|food|*|{N} <steht|stehen> schon auf dem Tisch.
NS|stehen|meal|*|{N} <steht|stehen> schon auf dem Tisch.
NS|sein|food|*|{N} <ist|sind> frisch und billig.
NS|sein|food|*|{N} <ist|sind> leider schon alle.
NS|sein|drink|*|{N} <ist|sind> leider schon alle.
NS|passen|clothes|*|{N} <passt|passen> mir leider nicht.
NS|sein|clothes|*|{N} <ist|sind> mir viel zu groß.
NS|hängen|hang|*|{N} <hängt|hängen> im Schrank.
NS|sein|shop|*|{N} <ist|sind> heute leider geschlossen.
NS|öffnen|shop|*|{N} <öffnet|öffnen> um acht Uhr.
NS|haben|shop|*|{N} <hat|haben> bis 20 Uhr geöffnet.
NS|liegen|building|*|{N} <liegt|liegen> ganz am Stadtrand.
NS|anhalten|lasting|*|{N} <hält|halten> den ganzen Tag an.
NS|beginnen|event|*|{N} <beginnt|beginnen> pünktlich um acht Uhr.
NS|dauern|event|*|{N} <dauert|dauern> diesmal ziemlich lange.
NS|sein|nice|*|{N} <war|waren> wirklich schön.
NS|wehtun|body|*|{N} <tut|tun> mir schon seit gestern weh.
NS|wachsen|plant|*|{N} <wächst|wachsen> sehr schnell.
NS|sein|room|*|{N} <ist|sind> nicht groß, aber gemütlich.
NS|haben|person|*|{N} <hat|haben> heute Geburtstag.
NS|haben|job|*|{N} <hat|haben> heute frei.
NS|anfangen|job|*|{N} <fängt|fangen> um sieben Uhr an.
NS|helfen|job|*|{N} <hilft|helfen> uns gern.
NS|besuchen|family|*|{N} <besucht|besuchen> uns am Wochenende.
NS|besuchen|friend|*|{N} <besucht|besuchen> uns am Wochenende.
NS|zurückrufen|adult|*|{N} <ruft|rufen> gleich zurück.
NS|sein|loud|*|{N} <ist|sind> heute wieder sehr laut.
NP|sein|person|*|Das <ist|sind> {N} von nebenan.
NP|sein|shop|*|Das <ist|sind> {N} in unserer Straße.
NP|sein|obj|*|Das <ist|sind> {N} von meiner Schwester.
NS|sein|obj|*|Wo <ist|sind> {N}?
NS|sein|person|*|Wo <ist|sind> {N}?
NS|sein|place|*|Wo <ist|sind> {N}?
NS|sein|animal|*|Wo <ist|sind> {N}?
NS|kommen|transit|*|Wann <kommt|kommen> {N}?
NS|kommen|adult|*|Wann <kommt|kommen> {N}?
NS|sein|shop|*|<Ist|Sind> {N} heute geöffnet?
NS|sein|free|*|<Ist|Sind> {N} noch frei?
NS|kosten|obj|*|Was <kostet|kosten> {N}?
NS|kosten|food|*|Was <kostet|kosten> {N}?
NS|schmecken|food|*|<Schmeckt|Schmecken> dir {N}?
NS|schmecken|drink|*|<Schmeckt|Schmecken> dir {N}?
NS|gefallen|obj|*|<Gefällt|Gefallen> dir {N}?
NS|gefallen|scene|*|<Gefällt|Gefallen> dir {N}?
NS|gefallen|room|*|<Gefällt|Gefallen> dir {N}?
NS|gehören|thing|*|<Gehört|Gehören> dir {N}?
NS|gehören|clothes|*|<Gehört|Gehören> dir {N}?

# ================= AKKUSATIV =================
AV|sehen|person|*|Ich sehe {N} jeden Morgen an der Haltestelle.
AV|kennen|person|*|Kennst du {N} schon?
AV|kennen|place|*|Kennst du {N} schon?
AV|kennen|media|*|Kennst du {N} schon?
AV|treffen|adult|*|Ich treffe {N} morgen im Café.
AV|besuchen|family|*|Wir besuchen {N} am Sonntag.
AV|besuchen|friend|*|Wir besuchen {N} am Sonntag.
AV|besuchen|visit|*|Am Samstag besuchen wir {N}.
AV|einladen|adult|*|Ich lade {N} zu meiner Party ein.
AV|anrufen|adult|*|Ich rufe {N} heute Abend an.
AV|fragen|adult|*|Ich frage {N} nach dem Weg.
AV|hören|person|*|Ich höre {N} laut lachen.
AV|abholen|family|*|Ich hole {N} vom Bahnhof ab.
AV|abholen|friend|*|Ich hole {N} vom Bahnhof ab.
AV|vermissen|family|*|Ich vermisse {N} sehr.
AV|vermissen|friend|*|Ich vermisse {N} sehr.
AV|vermissen|pet|*|Ich vermisse {N} sehr.
AV|lieben|family|*|Ich liebe {N} über alles.
AV|lieben|pet|*|Ich liebe {N} über alles.
AV|brauchen|obj|*|Ich brauche dringend {N}.
AV|brauchen|job|*|Ich brauche dringend {N}.
AV|brauchen|food|*|Ich brauche dringend {N}.
AV|brauchen|drink|*|Ich brauche dringend {N}.
AV|kaufen|obj|*|Ich kaufe {N} im Internet.
AV|kaufen|food|*|Ich kaufe {N} auf dem Markt.
AV|kaufen|drink|*|Ich kaufe {N} auf dem Markt.
AV|verkaufen|obj|*|Mein Nachbar verkauft {N}.
AV|essen|food|*|Ich esse {N} sehr gern.
AV|trinken|drink|*|Ich trinke {N} am liebsten kalt.
AV|kochen|cook|*|Heute Abend koche ich {N}.
AV|backen|bake|*|Ich backe {N} für die Party.
AV|bestellen|food|*|Im Restaurant bestelle ich {N}.
AV|bestellen|drink|*|Im Restaurant bestelle ich {N}.
AV|bezahlen|meal|*|Wer bezahlt {N}?
AV|bezahlen|drink|*|Wer bezahlt {N}?
AV|lesen|text|*|Ich lese {N} am Wochenende.
AV|schreiben|write|*|Ich schreibe {N} heute noch.
AV|beantworten|answer|*|Ich beantworte {N} gleich.
AV|hören|listen|*|Ich höre {N} jeden Tag im Auto.
AV|sehen|watch|*|Am Abend sehen wir {N}.
AV|öffnen|open|*|Kannst du bitte {N} öffnen?
AV|schließen|close|mfn|Ich schließe {N} und gehe nach Hause.
AV|tragen|clothes|mfn|Heute trage ich {N}.
AV|tragen|shoe|p|Heute trage ich {N}.
AV|anziehen|clothes|mfn|Ich ziehe {N} an, weil es kalt ist.
AV|anziehen|shoe|p|Ich ziehe {N} an, weil es draußen nass ist.
AV|suchen|thing|*|Ich suche {N} schon seit einer Stunde.
AV|suchen|media|*|Ich suche {N} schon seit einer Stunde.
AV|suchen|pet|*|Ich suche {N} schon seit einer Stunde.
AV|finden|thing|*|Endlich finde ich {N} wieder.
AV|finden|clothes|*|Endlich finde ich {N} wieder.
AV|finden|pet|*|Endlich finde ich {N} wieder.
AV|verlieren|thing|*|Ich habe {N} im Bus verloren.
AV|verlieren|clothes|*|Ich habe {N} im Bus verloren.
AV|vergessen|thing|*|Leider habe ich {N} zu Hause vergessen.
AV|vergessen|media|*|Leider habe ich {N} zu Hause vergessen.
AV|mitbringen|thing|*|Kannst du bitte {N} mitbringen?
AV|mitbringen|food|*|Kannst du bitte {N} mitbringen?
AV|mitbringen|drink|*|Kannst du bitte {N} mitbringen?
AV|mitnehmen|pack|*|Ich nehme {N} mit in den Urlaub.
AV|reparieren|repair|*|Mein Bruder repariert {N}.
AV|putzen|clean|*|Ich putze {N} jeden Samstag.
AV|aufräumen|room|*|Am Wochenende räume ich {N} auf.
AV|waschen|wash|*|Ich wasche {N} heute noch.
AV|streicheln|pet|*|Das Kind streichelt {N}.
AV|füttern|animal|*|Jeden Morgen füttere ich {N}.
AV|beobachten|animal|*|Wir beobachten {N} beim Spaziergang.
AV|malen|paint|*|Meine Tochter malt {N}.
AV|mögen|person|*|Ich mag {N} sehr.
AV|mögen|animal|*|Ich mag {N} sehr.
AV|mögen|food|*|Ich mag {N} sehr.
AV|mögen|drink|*|Ich mag {N} sehr.
AV|mögen|weather|*|Ich mag {N} sehr.
AV|haben|obj|*|Wir haben {N} schon seit zwei Jahren.
AV|haben|pet|*|Wir haben {N} schon seit zwei Jahren.
AV|verstehen|adult|*|Ich verstehe {N} nicht.
AV|verstehen|abstract|*|Ich verstehe {N} nicht.
AV|machen|do|mfn|Ich mache {N} heute Abend.
AV|organisieren|organize|*|Wir organisieren {N} für nächsten Monat.
AV|planen|plan|*|Wir planen {N} schon lange.
AV|verpassen|miss|mfn|Ich verpasse fast immer {N}.
AV|nehmen|ride|*|Ich nehme {N} zur Arbeit.
AV|reservieren|reserve|*|Ich reserviere {N} für heute Abend.
AV|besichtigen|sight|*|Wir besichtigen {N} am Nachmittag.
AV|sehen|scene|*|Von hier aus sieht man {N}.
AV|brechen|break|mfn|Er hat sich {N} gebrochen.
AV|untersuchen|body|*|Der Arzt untersucht {N}.
AV|einschalten|device|*|Kannst du bitte {N} einschalten?
AV|ausschalten|device|*|Ich schalte {N} kurz aus.
AV|benutzen|device|*|Ich benutze {N} jeden Tag.
AV|gießen|plant|*|Ich gieße {N} jeden Morgen.
AV|bekommen|receive|*|Ich bekomme {N} morgen per Post.
AV|schenken|gift|*|Ich schenke meiner Mutter {N} zum Geburtstag.
AP|für|family|*|Das ist ein Geschenk für {N}.
AP|für|friend|*|Das ist ein Geschenk für {N}.
AP|für|pet|*|Das ist ein Geschenk für {N}.
AP|für|obj|*|Ich zahle nicht viel für {N}.
AP|für|drink|*|Ich zahle nicht viel für {N}.
AP|ohne|family|*|Ich kann nicht ohne {N} leben.
AP|ohne|drink|*|Ich kann nicht ohne {N} leben.
AP|ohne|device|*|Ich kann nicht ohne {N} leben.
AP|ohne|thing|mfn|Er ist ohne {N} aus dem Haus gegangen.
AP|durch|through|*|Wir fahren mit dem Rad durch {N}.
AP|gegen|hit|*|Der Ball fliegt gegen {N}.
AP|gegen|friend|*|Wir spielen morgen Fußball gegen {N}.
AP|gegen|job|*|Wir spielen morgen Fußball gegen {N}.
AP|gegen|group|*|Wir spielen morgen Fußball gegen {N}.
AP|um|around|*|Wir gehen jeden Sonntag um {N} spazieren.
AP|warten auf|transit|mfn|Ich warte schon lange auf {N}.
AP|warten auf|adult|*|Ich warte schon lange auf {N}.
AP|warten auf|meal|*|Ich warte schon lange auf {N}.
AP|sich freuen auf|nice|*|Ich freue mich schon auf {N}.
AP|sich freuen auf|family|*|Ich freue mich schon auf {N}.
AP|denken an|family|*|Ich denke oft an {N}.
AP|denken an|friend|*|Ich denke oft an {N}.
AP|denken an|pet|*|Ich denke oft an {N}.
AP|denken an|place|*|Ich denke oft an {N}.
AP|denken an|nice|*|Ich denke oft an {N}.
AP|sich interessieren für|media|*|Ich interessiere mich sehr für {N}.
AP|sich interessieren für|animal|*|Ich interessiere mich sehr für {N}.
AP|sich interessieren für|sport|*|Ich interessiere mich sehr für {N}.
AP|sich interessieren für|device|*|Ich interessiere mich sehr für {N}.
AP|sich ärgern über|weather|*|Ich ärgere mich über {N}.
AP|sich ärgern über|abstract|*|Ich ärgere mich über {N}.
AP|sich ärgern über|transit|*|Ich ärgere mich über {N}.
AP|sich freuen über|gift|*|Ich freue mich sehr über {N}.
AP|sprechen über|family|*|Wir sprechen oft über {N}.
AP|sprechen über|friend|*|Wir sprechen oft über {N}.
AP|sprechen über|media|*|Wir sprechen oft über {N}.
AP|sich kümmern um|pet|*|Ich kümmere mich um {N}.
AP|sich kümmern um|family|*|Ich kümmere mich um {N}.
AP|sich kümmern um|plant|*|Ich kümmere mich um {N}.
AW|in|go|mf|Ich gehe jetzt in {N}.
AW|auf|surface|mfn|Ich stelle die Flasche auf {N}.
AW|über|coverable|mfn|Ich lege die Decke über {N}.
AW|hinter|hideplace|mfn|Ich stelle den Koffer hinter {N}.
AW|hinter|adult|*|Das Kind stellt sich hinter {N}.
AW|unter|under|mfn|Ich stelle den Korb unter {N}.
AW|vor|building|mfn|Der Fahrer stellt das Auto vor {N}.
AW|neben|furniture|mfn|Ich stelle die Pflanze neben {N}.
AW|neben|person|*|Ich setze mich neben {N}.
AW|vor|person|*|Er stellt sich vor {N}.
AW|zwischen|person|p|Ich setze mich zwischen {N}.
AW|an|wall|mfn|Ich lehne das Fahrrad an {N}.
AW|auf|seat|*|Ich setze die Katze auf {N}.
AW|in|container|mf|Ich lege das Handy in {N}.

# ================= DATIV =================
DV|helfen|child|*|Ich helfe {N} bei den Hausaufgaben.
DV|helfen|adult|*|Kannst du {N} beim Umzug helfen?
DV|danken|adult|*|Ich danke {N} für die Hilfe.
DV|danken|child|*|Ich danke {N} für die Hilfe.
DV|gratulieren|person|*|Wir gratulieren {N} zum Geburtstag.
DV|antworten|adult|*|Der Lehrer antwortet {N} sofort.
DV|antworten|child|*|Der Lehrer antwortet {N} sofort.
DV|zuhören|person|*|Ich höre {N} gern zu.
DV|folgen|person|*|Der Hund folgt {N} überallhin.
DV|gehören|person|*|Das Fahrrad gehört {N}.
DV|gefallen|person|*|Das Geschenk gefällt {N} sehr.
DV|passen|person|*|Die Jacke passt {N} nicht.
DV|schmecken|person|*|Das Essen schmeckt {N} nicht.
DV|schmecken|pet|*|Das Futter schmeckt {N} nicht.
DV|glauben|adult|*|Ich glaube {N} kein Wort.
DV|vertrauen|adult|*|Ich vertraue {N} vollkommen.
DV|begegnen|adult|*|Ich bin {N} gestern im Park begegnet.
DV|winken|adult|*|Das Kind winkt {N} zum Abschied.
DV|raten|adult|*|Der Arzt rät {N} zu mehr Sport.
DV|erlauben|adult|*|Meine Mutter erlaubt {N} das nicht.
DV|erlauben|child|*|Meine Mutter erlaubt {N} das nicht.
DI|geben|person|*|Ich gebe {N} das Buch.
DI|geben|animal|*|Ich gebe {N} jeden Tag frisches Futter.
DI|schenken|person|*|Wir schenken {N} eine Blume.
DI|zeigen|adult|*|Ich zeige {N} unser neues Haus.
DI|zeigen|child|*|Ich zeige {N} unser neues Haus.
DI|schicken|adult|*|Ich schicke {N} eine Nachricht.
DI|schicken|child|*|Ich schicke {N} eine Nachricht.
DI|erklären|child|*|Die Mutter erklärt {N} die Aufgabe.
DI|bringen|person|*|Der Kellner bringt {N} das Essen.
DI|kaufen|family|*|Ich kaufe {N} ein Eis.
DI|kaufen|friend|*|Ich kaufe {N} ein Eis.
DI|kaufen|child|*|Ich kaufe {N} ein Eis.
DI|erzählen|person|*|Meine Oma erzählt {N} eine Geschichte.
DI|leihen|adult|*|Kannst du {N} dein Fahrrad leihen?
DI|sagen|adult|*|Ich sage {N} die Wahrheit.
DI|sagen|child|*|Ich sage {N} die Wahrheit.
DI|kochen|person|*|Ich koche {N} eine Suppe.
DI|mitbringen|person|*|Ich bringe {N} Blumen mit.
DI|verkaufen|adult|*|Die Verkäuferin verkauft {N} zwei Brötchen.
DI|verkaufen|child|*|Die Verkäuferin verkauft {N} zwei Brötchen.
DP|mit|adult|*|Ich gehe heute mit {N} ins Kino.
DP|mit|child|*|Ich gehe heute mit {N} ins Kino.
DP|mit|adult|*|Wir sind gestern mit {N} spazieren gegangen.
DP|mit|family|*|Wir sind gestern mit {N} spazieren gegangen.
DP|mit|ride|mfn|Ich fahre jeden Tag mit {N} zur Arbeit.
DP|mit|point|*|Sie zeigt mit {N} auf das Bild.
DP|mit|adult|*|Ich telefoniere jeden Tag mit {N}.
DP|nach|after|*|Nach {N} gehe ich sofort nach Hause.
DP|aus|come_from|*|Er kommt gerade aus {N}.
DP|aus|container|mfn|Ich nehme das Buch aus {N}.
DP|seit|since|*|Ich bin seit {N} sehr müde.
DP|bei|host|f|Ich wohne zurzeit bei {N}.
DP|bei|parents|p|Ich wohne zurzeit bei {N}.
DP|bei|job|f|Ich war heute Morgen bei {N}.
DP|von|adult|fp|Das Geschenk ist von {N}.
DP|von|host|f|Ich habe lange nichts von {N} gehört.
DP|von|parents|p|Ich habe lange nichts von {N} gehört.
DP|gegenüber|building|mfn|Die Haltestelle liegt gegenüber {N}.
DP|außer|person|*|Alle sind da, außer {N}.
DW|neben|furniture|mfn|Die Pflanze steht neben {N}.
DW|neben|person|*|Ich sitze im Kino neben {N}.
DW|vor|building|mfn|Das Auto steht vor {N}.
DW|vor|shop|mfn|Ich warte vor {N} auf dich.
DW|hinter|hideplace|mfn|Die Katze schläft hinter {N}.
DW|unter|under|mfn|Die Katze schläft unter {N}.
DW|über|over|mfn|Die Lampe hängt über {N}.
DW|zwischen|building|mfn|Die Haltestelle liegt zwischen {N} und dem Park.
DW|auf|surface|mfn|Die Tasse steht auf {N}.
DW|auf|seat|mfn|Das Kind sitzt auf {N}.
DW|in|work|f|Meine Schwester arbeitet in {N}.
DW|in|live|f|Wir wohnen in {N}.
DW|an|wait_at|f|Wir warten an {N}.
DW|an|wall|f|Das Bild hängt an {N}.

# ================= GENITIV =================
GA|Auto|person|*|Das ist das Auto {N}.
GA|Fahrrad|person|*|Wo ist das Fahrrad {N}?
GA|Handy|person|*|Das Handy {N} liegt auf dem Tisch.
GA|Tasche|person|*|Ich finde die Tasche {N} nicht.
GA|Name|person|*|Der Name {N} ist mir leider entfallen.
GA|Geburtstag|person|*|Wann ist der Geburtstag {N}?
GA|Haus|person|*|Das Haus {N} steht am Stadtrand.
GA|Hund|person|*|Der Hund {N} bellt schon wieder.
GA|Wohnung|person|*|Die Wohnung {N} ist sehr hell.
GA|Stimme|person|*|Ich kenne die Stimme {N}.
GA|Tür|building|mfn|Die Tür {N} ist kaputt.
GA|Tür|vehicle|mfn|Die Tür {N} ist kaputt.
GA|Dach|building|mfn|Das Dach {N} ist rot.
GA|Eingang|building|mfn|Wo ist der Eingang {N}?
GA|Garten|grounds|mfn|Der Garten {N} ist wunderschön.
GA|Garten|person|*|Der Garten {N} ist wunderschön.
GA|Preis|obj|mfn|Wie hoch ist der Preis {N}?
GA|Preis|food|mfn|Wie hoch ist der Preis {N}?
GA|Farbe|obj|mfn|Die Farbe {N} gefällt mir.
GA|Größe|room|mfn|Die Größe {N} ist ideal.
GA|Größe|building|mfn|Die Größe {N} ist ideal.
GA|Ende|story|mfn|Das Ende {N} war traurig.
GA|Anfang|story|mfn|Der Anfang {N} war langweilig.
GA|Seite|readable|mfn|Die letzte Seite {N} fehlt.
GA|Titel|title|mfn|Wie heißt der Titel {N}?
GA|Besitzer|pet|*|Wer ist der Besitzer {N}?
GA|Besitzer|building|mfn|Wer ist der Besitzer {N}?
GA|Fahrer|transit|mfn|Der Fahrer {N} ist sehr freundlich.
GA|Direktor|institution|mfn|Der Direktor {N} kommt aus Italien.
GP|wegen|cause|mfn|Wegen {N} komme ich heute zu spät.
GP|wegen|badweather|*|Wegen {N} bleiben wir heute zu Hause.
GP|trotz|badweather|*|Trotz {N} gehen wir spazieren.
GP|trotz|cause|mfn|Trotz {N} kommt er zur Arbeit.
GP|während|show|*|Während {N} darf man nicht telefonieren.
GP|während|trip|*|Während {N} sind wir viel gewandert.
GP|während|period|mfn|Während {N} ist es hier meistens ruhig.
GP|statt|swap|*|Statt {N} nehme ich lieber Tee.
GP|statt|ride|*|Statt {N} gehe ich heute zu Fuß.
GP|außerhalb|settle|*|Außerhalb {N} gibt es viele Felder.
GP|innerhalb|within|mfn|Innerhalb {N} bekommst du eine Antwort.
"""

# One sentence found unnatural in the final proof-read ("in den Balkon": German says "auf den Balkon").
# Swapped for an equivalent masculine noun; kept as a post-fix so the reviewed selection is unchanged.
POST_FIXES = {"Ich gehe jetzt in ___ Balkon.": ("Balkon", "Keller")}


# ======================================================================
#  Personal pronouns (1st / 2nd person).  The 3rd-person exercises re-use FRAMES above.
#  PRON_FRAMES      same format as FRAMES, the subject is always a 3rd person so the pronoun is never reflexive
#  PRON_PREDICATES  fills "Ich/Du/Wir/Ihr <sein> ___." which tells the learner who the pronoun is
#  PRON_DIALOGUES   answer|person asked|text with {P}|verb   (Nominativ: question -> reply)
# ======================================================================
PRON_FRAMES = """
AV|untersuchen|x|*|Der Arzt untersucht {N} gründlich.
AV|anrufen|x|*|Mein Chef ruft {N} morgen an.
AV|besuchen|x|*|Meine Großmutter besucht {N} am Sonntag.
AV|abholen|x|*|Der Fahrer holt {N} vom Bahnhof ab.
AV|fragen|x|*|Die Lehrerin fragt {N} nach der Hausaufgabe.
AV|einladen|x|*|Unser Nachbar lädt {N} zum Grillen ein.
AV|grüßen|x|*|Die Verkäuferin grüßt {N} jeden Morgen freundlich.
AV|vermissen|x|*|Meine Freundin vermisst {N} sehr.
AV|verstehen|x|*|Der Lehrer versteht {N} gut.
AV|sehen|x|*|Der Kellner sieht {N} sofort.
AV|hören|x|*|Die Nachbarin hört {N} durch die Wand.
AV|kennen|x|*|Der Polizist kennt {N} schon lange.
AV|treffen|x|*|Meine Kollegin trifft {N} morgen im Café.
AV|brauchen|x|*|Die Kinder brauchen {N} dringend.
AV|lieben|x|*|Mein Hund liebt {N} über alles.
AV|begrüßen|x|*|Der Gastgeber begrüßt {N} an der Tür.
AV|bringen|x|*|Das Taxi bringt {N} zum Flughafen.
AV|beraten|x|*|Die Verkäuferin berät {N} freundlich.
AV|erkennen|x|*|Mein Onkel erkennt {N} sofort.
AV|suchen|x|*|Die Polizei sucht {N} schon seit Stunden.
AP|für|x|*|Der Chef hat ein Geschenk für {N} gekauft.
AP|ohne|x|*|Der Bus fährt nicht ohne {N} ab.
AP|gegen|x|*|Die Nachbarn haben nichts gegen {N}.
AP|warten auf|x|*|Meine Eltern warten schon auf {N}.
AP|denken an|x|*|Meine Oma denkt oft an {N}.
AP|sich freuen auf|x|*|Die Kinder freuen sich schon auf {N}.
AP|sich kümmern um|x|*|Meine Schwester kümmert sich um {N}.
AW|neben|x|*|Der Lehrer setzt sich neben {N}.
DV|helfen|x|*|Der Lehrer hilft {N} bei der Aufgabe.
DV|danken|x|*|Mein Chef dankt {N} für die Arbeit.
DV|gratulieren|x|*|Unsere Nachbarn gratulieren {N} zum Geburtstag.
DV|antworten|x|*|Der Kellner antwortet {N} freundlich.
DV|zuhören|x|*|Die Lehrerin hört {N} aufmerksam zu.
DV|folgen|x|*|Der Hund folgt {N} überallhin.
DV|gehören|x|*|Das Fahrrad vor der Tür gehört {N}.
DV|gefallen|x|*|Die neue Wohnung gefällt {N} sehr.
DV|passen|x|*|Die Jacke passt {N} perfekt.
DV|schmecken|x|*|Die Suppe schmeckt {N} nicht.
DV|glauben|x|*|Meine Eltern glauben {N} kein Wort.
DV|vertrauen|x|*|Der Chef vertraut {N} vollkommen.
DV|begegnen|x|*|Der Nachbar begegnet {N} jeden Morgen im Treppenhaus.
DV|winken|x|*|Die Kinder winken {N} zum Abschied.
DI|geben|x|*|Die Ärztin gibt {N} ein Rezept.
DI|zeigen|x|*|Der Nachbar zeigt {N} den Garten.
DI|schenken|x|*|Meine Tante schenkt {N} ein Buch.
DI|schicken|x|*|Mein Bruder schickt {N} eine Nachricht.
DI|erklären|x|*|Die Lehrerin erklärt {N} die Aufgabe.
DI|bringen|x|*|Der Kellner bringt {N} das Essen.
DI|erzählen|x|*|Meine Oma erzählt {N} eine Geschichte.
DI|sagen|x|*|Der Arzt sagt {N} die Wahrheit.
DI|kochen|x|*|Meine Mutter kocht {N} eine Suppe.
DI|leihen|x|*|Mein Freund leiht {N} sein Fahrrad.
DP|mit|x|*|Die Lehrerin spricht gern mit {N}.
DP|mit|x|*|Meine Freunde gehen heute mit {N} ins Kino.
DP|bei|x|*|Mein Onkel wohnt zurzeit bei {N}.
DP|von|x|*|Das Geschenk ist von {N}.
DP|zu|x|*|Der Arzt kommt heute zu {N}.
DP|gegenüber|x|*|Der Lehrer sitzt {N} gegenüber.
DW|neben|x|*|Der Lehrer sitzt im Bus neben {N}.
"""

PRON_PREDICATES = """
müde
neu hier
nervös
spät dran
in Eile
fertig
allein
hungrig
gut gelaunt
pünktlich
zu Hause
im Stress
"""

PRON_DIALOGUES = """
ich|du|Hast du morgen Zeit? – Ja, {P} habe morgen Zeit.|habe
ich|du|Kommst du heute Abend? – Ja, {P} komme gern.|komme
ich|du|Sprichst du Deutsch? – Ja, {P} spreche ein bisschen Deutsch.|spreche
ich|du|Wohnst du in Berlin? – Nein, {P} wohne in Köln.|wohne
ich|du|Arbeitest du heute? – Ja, {P} arbeite bis fünf Uhr.|arbeite
ich|du|Bist du müde? – Ja, {P} bin sehr müde.|bin
ich|du|Hast du Hunger? – Ja, {P} habe großen Hunger.|habe
ich|du|Kannst du mir helfen? – Ja, {P} kann dir helfen.|kann
ich|du|Trinkst du Kaffee? – Nein, {P} trinke lieber Tee.|trinke
ich|du|Fährst du mit dem Bus? – Nein, {P} fahre mit dem Fahrrad.|fahre
ich|du|Kochst du heute? – Ja, {P} koche Nudeln.|koche
ich|du|Spielst du Fußball? – Ja, {P} spiele jeden Samstag.|spiele
ich|du|Liest du gern? – Ja, {P} lese jeden Abend ein Buch.|lese
ich|du|Gehst du morgen ins Kino? – Ja, {P} gehe um acht.|gehe
ich|du|Brauchst du Hilfe? – Nein, {P} brauche keine Hilfe.|brauche
ich|du|Bist du fertig? – Ja, {P} bin gleich da.|bin
ich|du|Hast du ein Auto? – Nein, {P} habe kein Auto.|habe
ich|du|Isst du Fleisch? – Nein, {P} esse kein Fleisch.|esse
ich|du|Schläfst du schon? – Nein, {P} schlafe noch nicht.|schlafe
wir|ihr|Kommt ihr morgen? – Ja, {P} kommen um acht.|kommen
wir|ihr|Habt ihr Hunger? – Ja, {P} haben großen Hunger.|haben
wir|ihr|Wohnt ihr hier? – Ja, {P} wohnen seit zwei Jahren hier.|wohnen
wir|ihr|Seid ihr müde? – Ja, {P} sind sehr müde.|sind
wir|ihr|Spielt ihr Fußball? – Ja, {P} spielen jeden Sonntag.|spielen
wir|ihr|Fahrt ihr in den Urlaub? – Ja, {P} fahren nach Italien.|fahren
wir|ihr|Arbeitet ihr heute? – Nein, {P} haben frei.|haben
wir|ihr|Kocht ihr heute Abend? – Ja, {P} kochen für alle.|kochen
wir|ihr|Braucht ihr Hilfe? – Nein, {P} schaffen das allein.|schaffen
wir|ihr|Lernt ihr Deutsch? – Ja, {P} lernen jeden Tag.|lernen
wir|ihr|Geht ihr mit ins Kino? – Nein, {P} bleiben zu Hause.|bleiben
wir|ihr|Wartet ihr schon lange? – Ja, {P} warten seit einer Stunde.|warten
du|ich|Habe ich recht? – Ja, {P} hast recht.|hast
du|ich|Störe ich? – Nein, {P} störst nicht.|störst
du|ich|Bin ich zu spät? – Nein, {P} bist pünktlich.|bist
du|ich|Kann ich dir helfen? – Ja, {P} kannst mir helfen.|kannst
du|ich|Darf ich hier sitzen? – Ja, {P} darfst hier sitzen.|darfst
du|ich|Muss ich morgen kommen? – Ja, {P} musst um acht da sein.|musst
du|ich|Soll ich Kaffee kochen? – Ja, {P} kannst gern Kaffee kochen.|kannst
du|ich|Habe ich Post? – Ja, {P} hast einen Brief bekommen.|hast
du|ich|Bin ich dran? – Ja, {P} bist als Nächster dran.|bist
du|ich|Habe ich noch Zeit? – Ja, {P} hast noch zehn Minuten.|hast
"""
