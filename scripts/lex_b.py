"""Level B data: work, study, bureaucracy, travel, media, society (roughly B1 + B2).
Same format as lex_a.py - see the docstring there."""

NOUNS = """
# ---- people at work / in institutions
Mitarbeiter|m|Mitarbeiter|s|person adult job hire guide employee
Mitarbeiterin|f|Mitarbeiterinnen|-|person adult job hire guide employee
Kollege|m|Kollegen|W:n|person adult job guide employee
Kollegin|f|Kolleginnen|-|person adult job guide employee
Chef|m|Chefs|s|person adult job authority speaker manager
Chefin|f|Chefinnen|-|person adult job authority speaker manager
Leiter|m|Leiter|s|person adult job authority speaker manager
Leiterin|f|Leiterinnen|-|person adult job authority speaker manager
Direktor|m|Direktoren|s|person adult job authority speaker manager
Direktorin|f|Direktorinnen|-|person adult job authority speaker manager
Ingenieur|m|Ingenieure|s|person adult job hire
Ingenieurin|f|Ingenieurinnen|-|person adult job hire
Techniker|m|Techniker|s|person adult job hire
Technikerin|f|Technikerinnen|-|person adult job hire
Berater|m|Berater|s|person adult job hire expert
Beraterin|f|Beraterinnen|-|person adult job hire expert
Anwalt|m|Anwälte|s|person adult job doctor authority
Anwältin|f|Anwältinnen|-|person adult job doctor authority
Richter|m|Richter|s|person adult job authority
Richterin|f|Richterinnen|-|person adult job authority
Arzt|m|Ärzte|es|person adult job doctor authority
Ärztin|f|Ärztinnen|-|person adult job doctor authority
Professor|m|Professoren|s|person adult job teacher speaker authority
Professorin|f|Professorinnen|-|person adult job teacher speaker authority
Dozent|m|Dozenten|W:en|person adult job teacher speaker
Dozentin|f|Dozentinnen|-|person adult job teacher speaker
Lehrer|m|Lehrer|s|person adult job teacher speaker
Lehrerin|f|Lehrerinnen|-|person adult job teacher speaker
Journalist|m|Journalisten|W:en|person adult job hire
Journalistin|f|Journalistinnen|-|person adult job hire
Politiker|m|Politiker|s|person adult job speaker authority
Politikerin|f|Politikerinnen|-|person adult job speaker authority
Experte|m|Experten|W:n|person adult job speaker expert
Expertin|f|Expertinnen|-|person adult job speaker expert
Künstler|m|Künstler|s|person adult job fund
Künstlerin|f|Künstlerinnen|-|person adult job fund
Student|m|Studenten|W:en|person adult student
Studentin|f|Studentinnen|-|person adult student
Schüler|m|Schüler|s|person child student
Schülerin|f|Schülerinnen|-|person child student
Kandidat|m|Kandidaten|W:en|person adult student votable customer
Kandidatin|f|Kandidatinnen|-|person adult student votable customer
Bewerber|m|Bewerber|s|person adult customer applicant hire
Bewerberin|f|Bewerberinnen|-|person adult customer applicant hire
Kunde|m|Kunden|W:n|person adult customer client
Kundin|f|Kundinnen|-|person adult customer client
Gast|m|Gäste|es|person adult customer
Patient|m|Patienten|W:en|person adult customer patient
Patientin|f|Patientinnen|-|person adult customer patient
Mieter|m|Mieter|s|person adult customer tenant client
Mieterin|f|Mieterinnen|-|person adult customer tenant client
Vermieter|m|Vermieter|s|person adult owner authority
Vermieterin|f|Vermieterinnen|-|person adult owner authority
Tourist|m|Touristen|W:en|person adult customer
Touristin|f|Touristinnen|-|person adult customer
Passagier|m|Passagiere|s|person adult customer
Passagierin|f|Passagierinnen|-|person adult customer
Bürger|m|Bürger|s|person adult customer client
Bürgerin|f|Bürgerinnen|-|person adult customer client
Nachbar|m|Nachbarn|W:n|person adult
Nachbarin|f|Nachbarinnen|-|person adult
Zeuge|m|Zeugen|W:n|person adult
Zeugin|f|Zeuginnen|-|person adult
Partner|m|Partner|s|person adult family partner
Partnerin|f|Partnerinnen|-|person adult family partner
Ehemann|m|Ehemänner|es|person adult family
Ehefrau|f|Ehefrauen|-|person adult family
Freund|m|Freunde|es|person adult family friend partner visit
Freundin|f|Freundinnen|-|person adult family friend partner visit
Sohn|m|Söhne|es|person adult child family visit
Tochter|f|Töchter|-|person adult child family visit
Enkel|m|Enkel|s|person child family visit
Enkelin|f|Enkelinnen|-|person child family visit
Kind|n|Kinder|es|person child family
Eltern|p|Eltern|-|person adult family visit
Geschwister|p|Geschwister|-|person adult family visit
Großeltern|p|Großeltern|-|person adult family visit
# ---- groups and organisations
Team|n|Teams|s|group club owner unit
Mannschaft|f|Mannschaften|-|group club
Familie|f|Familien|-|group society owner family roleholder
Verein|m|Vereine|s|group club fund unit owner
Partei|f|Parteien|-|group club votable authority
Regierung|f|Regierungen|-|group authority roleholder
Firma|f|Firmen|-|firm unit employer owner workplace institute group authority roleholder
Unternehmen|n|Unternehmen|s|firm unit employer owner group
Abteilung|f|Abteilungen|-|unit workplace group responsible
Behörde|f|Behörden|-|authority unit employer contact open firm institute
Amt|n|Ämter|es|authority unit open building contact
Bank|f|Banken|-|firm unit employer open building workplace institute roleholder
Versicherung|f|Versicherungen|-|firm employer contact pay conclude valid
Botschaft|f|Botschaften|-|authority contact building
Schule|f|Schulen|-|unit institute workplace building fund roleholder campus
Universität|f|Universitäten|-|unit institute attend building fund roleholder campus
Hochschule|f|Hochschulen|-|unit institute attend building campus
Bibliothek|f|Bibliotheken|-|unit open building fund workplace institute
Klinik|f|Kliniken|-|unit building workplace institute
Praxis|f|Praxen|-|open building workplace
Krankenhaus|n|Krankenhäuser|es|unit building
Rathaus|n|Rathäuser|es|building open sight authority
Museum|n|Museen|s|building open sight fund unit
Theater|n|Theater|s|building open sight fund owned
Stadion|n|Stadien|s|building sight
Kaufhaus|n|Kaufhäuser|es|building open owned
Einkaufszentrum|n|Einkaufszentren|s|building owned
Bahnhof|m|Bahnhöfe|es|building
Flughafen|m|Flughäfen|s|building
Hotel|n|Hotels|s|building bookable satisfy sight option owned
Restaurant|n|Restaurants|s|building owned
Bäckerei|f|Bäckereien|-|building shop owned
Supermarkt|m|Supermärkte|s|building shop owned
Apotheke|f|Apotheken|-|building shop
Kino|n|Kinos|s|building shop owned
Werkstatt|f|Werkstätten|-|workplace building owned
Fabrik|f|Fabriken|-|workplace building owned
Baustelle|f|Baustellen|-|cause
Kirche|f|Kirchen|-|building sight
Schloss|n|Schlösser|es|sight building
Burg|f|Burgen|-|sight
Altstadt|f|Altstädte|-|sight region centered
Hafen|m|Häfen|s|sight
# ---- places, regions, routes
Stadt|f|Städte|-|region origin into roleholder town populated centered throughable
Innenstadt|f|Innenstädte|-|region into populated throughable
Vorort|m|Vororte|es|region origin into town populated centered throughable
Dorf|n|Dörfer|es|region origin town populated centered throughable
Land|n|Länder|es|region origin populated centered throughable
Region|f|Regionen|-|region origin populated centered throughable
Gebirge|n|Gebirge|s|region crossing throughable
Küste|f|Küsten|-|region nature populated
Insel|f|Inseln|-|region populated centered
Wald|m|Wälder|es|region nature into throughable
Fluss|m|Flüsse|es|crossing
Brücke|f|Brücken|-|crossing
Grenze|f|Grenzen|-|crossing wait_at
Berg|m|Berge|es|crossing
Platz|m|Plätze|es|centered
Straße|f|Straßen|-|route
Autobahn|f|Autobahnen|-|route
Weg|m|Wege|es|route askabout
Ufer|n|Ufer|s|route
Kreuzung|f|Kreuzungen|-|wait_at
Haltestelle|f|Haltestellen|-|wait_at
Kasse|f|Kassen|-|wait_at counter responsible
Rezeption|f|Rezeptionen|-|wait_at contact
Schalter|m|Schalter|s|counter
Theke|f|Theken|-|counter
Schreibtisch|m|Schreibtische|es|counter under
Tisch|m|Tische|es|counter under
Schrank|m|Schränke|es|under container
Sofa|n|Sofas|s|under
Bett|n|Betten|es|under
# ---- home, technology
Wohnung|f|Wohnungen|-|home rent search viewing option
Haus|n|Häuser|es|home rent viewing
Ferienwohnung|f|Ferienwohnungen|-|home rent bookable viewing
Zimmer|n|Zimmer|s|home rent bookable viewing askabout
Küche|f|Küchen|-|home
Bad|n|Bäder|es|home
Balkon|m|Balkone|s|home
Treppe|f|Treppen|-|home
Unterkunft|f|Unterkünfte|-|bookable satisfy search askabout duty
Kühlschrank|m|Kühlschränke|es|tech buy goods under
Waschmaschine|f|Waschmaschinen|-|tech buy goods gadget
Heizung|f|Heizungen|-|tech
Aufzug|m|Aufzüge|es|tech
Handy|n|Handys|s|tech gadget buy goods carry payby luxury tool
Laptop|m|Laptops|s|tech gadget buy goods tool
Drucker|m|Drucker|s|tech gadget tool
Tastatur|f|Tastaturen|-|tech
Programm|n|Programme|s|tech software gadget buy download tool difficult
Software|f|-|-|tech software gadget tool difficult
Anwendung|f|Anwendungen|-|tech software gadget download tool
Update|n|Updates|s|software download
Homepage|f|Homepages|-|tech gadget
Internetverbindung|f|Internetverbindungen|-|tech
Netzwerk|n|Netzwerke|es|tech
Akku|m|Akkus|s|tech
Kamera|f|Kameras|-|gadget tool
Datei|f|Dateien|-|file download tool
Foto|n|Fotos|s|file send news
Dokument|n|Dokumente|es|file
Passwort|n|Passwörter|es|change
Einstellung|f|Einstellungen|-|change
# ---- transport and travel
Flug|m|Flüge|es|transit bookable buy satisfy show option
Zug|m|Züge|es|transit rail vehicle
Bus|m|Busse|ses|transit vehicle
Flugzeug|n|Flugzeuge|s|transit vehicle
S-Bahn|f|S-Bahnen|-|transit rail vehicle
U-Bahn|f|U-Bahnen|-|transit rail vehicle
Straßenbahn|f|Straßenbahnen|-|transit vehicle
Fähre|f|Fähren|-|transit vehicle
Auto|n|Autos|s|rent luxury buy obstacle option
Fahrrad|n|Fahrräder|es|rent buy
Boot|n|Boote|es|rent
Fahrkarte|f|Fahrkarten|-|buy id carry
Ticket|n|Tickets|s|buy id entry
Einladung|f|Einladungen|-|id pleasant entry
Koffer|m|Koffer|s|luggage carry
Gepäck|n|-|s|luggage carry duty
Reisetasche|f|Reisetaschen|-|luggage
Rucksack|m|Rucksäcke|s|luggage carry
Geldbeutel|m|Geldbeutel|s|carry
# ---- documents and paperwork
Ausweis|m|Ausweise|es|doc valid apply id carry entry
Reisepass|m|Reisepässe|es|doc valid apply id carry entry
Führerschein|m|Führerscheine|s|doc valid apply id carry
Visum|n|Visa|s|doc valid apply
Antrag|m|Anträge|s|doc sign submit fill check read send matter matter2 topic
Formular|n|Formulare|s|doc sign submit fill download send check difficult
Vertrag|m|Verträge|s|doc sign check read valid cancel conclude agree matter matter2 rule terms
Bewerbung|f|Bewerbungen|-|doc submit send check write matter2 worktask plan
Lebenslauf|m|Lebensläufe|es|doc submit send check write
Zeugnis|n|Zeugnisse|ses|doc mail
Bescheid|m|Bescheide|s|doc mail
Rechnung|f|Rechnungen|-|doc pay check send mail annoy matter2
Kündigung|f|Kündigungen|-|doc sign submit mail
Genehmigung|f|Genehmigungen|-|doc apply mail valid process
Bescheinigung|f|Bescheinigungen|-|doc apply mail
Steuererklärung|f|Steuererklärungen|-|doc submit fill
Anmeldung|f|Anmeldungen|-|doc fill submit duty
Unterschrift|f|Unterschriften|-|doc
Brief|m|Briefe|es|doc mail read write
E-Mail|f|E-Mails|-|write read
Bericht|m|Berichte|s|read write check send file evidence news topic worktask
Protokoll|n|Protokolle|s|write read file send
Artikel|m|Artikel|s|read news write
Paket|n|Pakete|s|mail
Bestellung|f|Bestellungen|-|duty matter2
Lieferung|f|Lieferungen|-|process
Angebot|n|Angebote|s|topic send option satisfy agree matter2 pleasant
Kredit|m|Kredite|s|apply
Konto|n|Konten|s|cancel
Mitgliedschaft|f|Mitgliedschaften|-|cancel
Abonnement|n|Abonnements|s|cancel
# ---- media and study
Interview|n|Interviews|s|news broadcast
Sendung|f|Sendungen|-|broadcast
Serie|f|Serien|-|broadcast
Dokumentation|f|Dokumentationen|-|broadcast
Umfrage|f|Umfragen|-|news assessed
Statistik|f|Statistiken|-|evidence
Studie|f|Studien|-|assessed evidence
Ergebnis|n|Ergebnisse|ses|check topic stat achieve improve satisfy evidence askabout
Buch|n|Bücher|es|read
Zeitung|f|Zeitungen|-|read means
Lehrbuch|n|Lehrbücher|es|read goods buy
Wörterbuch|n|Wörterbücher|es|goods buy tool
Thema|n|Themen|s|topic study
Übung|f|Übungen|-|study
Regel|f|Regeln|-|study rule terms
Lektion|f|Lektionen|-|study
Grammatik|f|-|-|study difficult
Wortschatz|m|-|es|
Studium|n|Studien|s|process starts task after option
Ausbildung|f|Ausbildungen|-|process starts conclude task option position after dolong
Praktikum|n|Praktika|s|starts position dolong
Stelle|f|Stellen|-|position search
Stipendium|n|Stipendien|s|apply position
Studienplatz|m|Studienplätze|es|position
Abschluss|m|Abschlüsse|es|achieve
Hausarbeit|f|Hausarbeiten|-|write task worktask
Referat|n|Referate|s|prep write giveTalk worktask
Vortrag|m|Vorträge|s|giveTalk show
Rede|f|Reden|-|giveTalk
Präsentation|f|Präsentationen|-|scheduled prep giveTalk file show after worktask success
Vorlesung|f|Vorlesungen|-|scheduled attend giveTalk show after
Seminar|n|Seminare|s|scheduled attend orga after
Sprachkurs|m|Sprachkurse|es|scheduled attend starts after dolong
Besprechung|f|Besprechungen|-|scheduled arrange prep show negotiation after
Sitzung|f|Sitzungen|-|scheduled arrange prep show course negotiation after
Konferenz|f|Konferenzen|-|scheduled orga prep show course negotiation after
Prüfung|f|Prüfungen|-|exam scheduled show assessed course after since success
Test|m|Tests|s|exam
Termin|m|Termine|s|arrange bookable askabout
# ---- ideas, politics, society
Vorschlag|m|Vorschläge|s|idea topic send option agree policy
Idee|f|Ideen|-|idea
Plan|m|Pläne|s|idea agree plan option worktask
Lösung|f|Lösungen|-|idea improve option satisfy success search doubt task agree worktask
Entscheidung|f|Entscheidungen|-|idea policy agree feel doubt
Meinung|f|Meinungen|-|idea feel value
Argument|n|Argumente|s|idea feel
Kompromiss|m|Kompromisse|ses|idea agree
Änderung|f|Änderungen|-|agree topic report risk difficult since
Reform|f|Reformen|-|policy law initiative
Gesetz|n|Gesetze|es|policy law rule terms
Regelung|f|Regelungen|-|policy law rule agree expect difficult terms
Vorschrift|f|Vorschriften|-|rule expect terms
Gebühr|f|Gebühren|-|pay rule price
Miete|f|Mieten|-|pay price dispute
Kaution|f|Kautionen|-|pay
Gehalt|n|Gehälter|es|price stat
Lohn|m|Löhne|es|price
Preis|m|Preise|es|price annoy attention askabout
Rente|f|Renten|-|price
Strafe|f|Strafen|-|pay price
Projekt|n|Projekte|s|topic initiative fund task responsible plan success option worktask
Problem|n|Probleme|s|topic solve trouble
Konflikt|m|Konflikte|s|solve trouble
Streit|m|-|es|solve avoid
Fehler|m|Fehler|s|avoid annoy responsible trouble
Schaden|m|Schäden|s|report damage responsible trouble
Unfall|m|Unfälle|s|report damage trouble cause experience
Stau|m|Staus|s|cause damage avoid annoy risk reduce
Verspätung|f|Verspätungen|-|cause avoid annoy risk difficulty damage
Streik|m|Streiks|s|cause risk experience
Sturm|m|Stürme|es|cause experience
Schnee|m|-|s|cause risk
Regen|m|-|s|cause risk
Lärm|m|-|s|cause dispute annoy reduce
Umbau|m|Umbauten|s|cause period after
Renovierung|f|Renovierungen|-|cause period initiative
Hitze|f|-|-|cause difficulty
Kälte|f|-|-|cause difficulty
Verkehr|m|-|s|society annoy risk econ reduce
Müll|m|-|s|dispute reduce
Krise|f|Krisen|-|trend crisis trouble
Situation|f|Situationen|-|trend crisis improve difficult
Lage|f|Lagen|-|crisis trend
Entwicklung|f|Entwicklungen|-|trend crisis
Klimawandel|m|-|s|crisis
Wirtschaft|f|-|-|econ trend society roleholder
Gesellschaft|f|Gesellschaften|-|society roleholder
Umwelt|f|-|-|nature roleholder
Klima|n|-|s|nature roleholder
Natur|f|-|-|nature
Energie|f|Energien|-|resource
Wasser|n|-|s|resource
Strom|m|-|s|resource
Geld|n|-|es|resource
Zeit|f|-|-|resource value attention
Bildung|f|-|-|value
Gesundheit|f|-|-|value
Sicherheit|f|-|-|value attention care responsible
Erfahrung|f|Erfahrungen|-|value memory means
Geduld|f|-|-|value
Ehrlichkeit|f|-|-|value
Vertrauen|n|-|s|value
Freiheit|f|Freiheiten|-|value
Zusammenarbeit|f|-|-|value improve
Kommunikation|f|-|-|value improve society
Freundschaft|f|Freundschaften|-|memory reason value
Beziehung|f|Beziehungen|-|improve trouble
Qualität|f|Qualitäten|-|improve attention
# ---- additions
Wand|f|Wände|-|wall
Tür|f|Türen|-|wall
Tafel|f|Tafeln|-|wall
Kalender|m|Kalender|s|hang
Schild|n|Schilder|es|hang list
Stadtplan|m|Stadtpläne|s|hang
Zettel|m|Zettel|s|hang
Bild|n|Bilder|es|hang
Liste|f|Listen|-|list
Seite|f|Seiten|-|list
Karte|f|Karten|-|list payby
Kreditkarte|f|Kreditkarten|-|payby
Gutschein|m|Gutscheine|es|payby
Mappe|f|Mappen|-|container contains
Schublade|f|Schubladen|-|container contains
Ordner|m|Ordner|s|container
Akte|f|Akten|-|contains
Broschüre|f|Broschüren|-|contains
Tasche|f|Taschen|-|container contains luggage
Erwartung|f|Erwartungen|-|expect
Anforderung|f|Anforderungen|-|expect
Aufgabe|f|Aufgaben|-|difficult solve task
Hindernis|n|Hindernisse|ses|obstacle
Radfahrer|m|Radfahrer|s|obstacle
Baum|m|Bäume|es|obstacle
Verhandlung|f|Verhandlungen|-|negotiation plan
Umzug|m|Umzüge|es|since report duty
Buchung|f|Buchungen|-|duty
Adresse|f|Adressen|-|
Verlust|m|Verluste|es|report
Antwort|f|Antworten|-|search
Ursache|f|Ursachen|-|search
Empfehlung|f|Empfehlungen|-|means
Zufall|m|Zufälle|s|
Anzeige|f|Anzeigen|-|means
Zukunft|f|-|-|hope
Kindheit|f|-|-|memory
Studienzeit|f|-|-|memory
Kundenservice|m|-|s|contact
Missverständnis|n|Missverständnisse|ses|matter
Notfall|m|Notfälle|s|matter
Irrtum|m|Irrtümer|s|matter
Parkplatz|m|Parkplätze|es|dispute
Geschenk|n|Geschenke|es|pleasant
Besuch|m|Besuche|es|pleasant
Hilfe|f|-|-|pleasant
Nachricht|f|Nachrichten|-|news
Rechtschreibung|f|-|-|attention
Arbeitslosigkeit|f|-|-|econ
Nachfrage|f|-|-|econ
Bevölkerung|f|-|-|econ
# ---- events, feelings, health, interests
Hochzeit|f|Hochzeiten|-|nice memory since after
Reise|f|Reisen|-|nice process memory initiative plan since luxury dolong after success
Urlaub|m|Urlaube|s|nice memory luxury period after
Ferien|p|Ferien|-|period
Wochenende|n|Wochenenden|s|nice
Ausflug|m|Ausflüge|es|nice orga initiative
Wanderung|f|Wanderungen|-|nice
Feier|f|Feiern|-|nice orga after
Konzert|n|Konzerte|es|nice after
Ziel|n|Ziele|es|achieve
Erfolg|m|Erfolge|es|achieve hope pleasant
Fortschritt|m|Fortschritte|s|achieve hope
Abenteuer|n|Abenteuer|s|experience
Überraschung|f|Überraschungen|-|experience pleasant success
Wahl|f|Wahlen|-|assessed after since
Untersuchung|f|Untersuchungen|-|assessed process after since
Behandlung|f|Behandlungen|-|process after
Operation|f|Operationen|-|process after since
Krankheit|f|Krankheiten|-|health cause since illness
Schmerz|m|Schmerzen|es|health
Grippe|f|-|-|health illness
Erkältung|f|Erkältungen|-|health illness
Verletzung|f|Verletzungen|-|health
Angst|f|Ängste|-|feel reason
Sorge|f|Sorgen|-|feel
Hoffnung|f|Hoffnungen|-|feel
Wut|f|-|-|feel reason
Neugier|f|-|-|reason
Höflichkeit|f|-|-|reason
Überzeugung|f|Überzeugungen|-|reason
Gewohnheit|f|Gewohnheiten|-|reason
Liebe|f|-|-|reason
Politik|f|-|-|interest
Kunst|f|Künste|-|interest
Geschichte|f|Geschichten|-|interest
Musik|f|-|-|interest
Technik|f|Techniken|-|interest
Sport|m|-|s|interest
Sprache|f|Sprachen|-|interest
Ordnung|f|-|-|care
Ruhe|f|-|-|care
Service|m|-|s|satisfy
Monat|m|Monate|s|period deadline
Woche|f|Wochen|-|period deadline
Jahr|n|Jahre|es|deadline
Tag|m|Tage|es|
Frist|f|Fristen|-|deadline attention
"""

FRAMES = """
# ================= NOMINATIV =================
NS|sein|job|*|Sobald {N} <da ist|da sind>, können wir mit der Besprechung anfangen.
NS|zurückkommen|adult|*|Ich weiß noch nicht, wann {N} aus dem Urlaub <zurückkommt|zurückkommen>.
NS|antworten|authority|*|Es dauert oft lange, bis {N} <antwortet|antworten>.
NS|entscheiden|authority|*|Am Ende <entscheidet|entscheiden> {N} über den Antrag.
NS|kündigen|job|*|Man erzählt sich, dass {N} überraschend <gekündigt hat|gekündigt haben>.
NS|sich bewerben|applicant|*|Für die Stelle im Marketing <bewirbt|bewerben> sich {N}.
NS|beraten|expert|*|{N} <berät|beraten> uns bei der Auswahl der richtigen Versicherung.
NS|leiten|manager|*|{N} <leitet|leiten> die Abteilung seit zwei Jahren.
NS|unterrichten|teacher|*|{N} <unterrichtet|unterrichten> Deutsch als Fremdsprache.
NS|warten|customer|*|Vor dem Schalter <wartet|warten> schon {N}.
NS|ankommen|customer|*|Wegen des Staus <ist|sind> {N} erst um Mitternacht angekommen.
NS|liegen|doc|*|{N} <liegt|liegen> seit Montag auf meinem Schreibtisch.
NS|fehlen|doc|*|Leider <fehlt|fehlen> noch {N}.
NS|ablaufen|valid|*|Bald <läuft|laufen> {N} ab.
NS|kommen|mail|*|Gestern <ist|sind> {N} mit der Post gekommen.
NS|gelten|rule|*|{N} <gilt|gelten> seit dem ersten Januar.
NS|steigen|price|*|In den letzten Jahren <ist|sind> {N} stark gestiegen.
NS|sinken|price|*|Im Vergleich zum Vorjahr <ist|sind> {N} gesunken.
NS|dauern|process|*|{N} <dauert|dauern> diesmal länger als geplant.
NS|stattfinden|scheduled|*|{N} <findet|finden> nächsten Dienstag statt.
NS|ausfallen|scheduled|*|Wegen Krankheit <fällt|fallen> {N} heute aus.
NS|beginnen|scheduled|*|Erst um zehn Uhr <beginnt|beginnen> {N}.
NS|liegen|stat|*|{N} <liegt|liegen> deutlich über dem Durchschnitt.
NS|sein|value|*|{N} <ist|sind> in dieser Situation besonders wichtig.
NS|wachsen|econ|*|{N} <wächst|wachsen> seit Jahren nur langsam.
NS|stehen|news|*|In der Zeitung <steht|stehen> {N} auf der ersten Seite.
NS|laufen|broadcast|*|Heute Abend <läuft|laufen> {N} im Fernsehen.
NS|funktionieren|tech|*|Seit gestern <funktioniert|funktionieren> {N} nicht mehr richtig.
NS|abstürzen|software|*|Schon wieder <stürzt|stürzen> {N} ab.
NS|ausfallen|tech|*|Mitten in der Nacht <ist|sind> {N} ausgefallen.
NS|kosten|buy|*|{N} <kostet|kosten> mehr, als ich erwartet hatte.
NS|haben|transit|*|Laut Anzeige <hat|haben> {N} heute leider Verspätung.
NS|liegen|building|*|{N} <liegt|liegen> mitten im Stadtzentrum.
NS|öffnen|open|*|Am Montag <öffnet|öffnen> {N} erst um neun Uhr.
NS|sein|open|*|Am Feiertag <ist|sind> {N} geschlossen.
NS|sein|bookable|*|Leider <ist|sind> {N} völlig ausgebucht.
NS|sein|health|*|{N} <ist|sind> schlimmer als erwartet.
NS|klingen|idea|*|{N} <klingt|klingen> auf den ersten Blick vernünftig.
NS|überzeugen|idea|*|Am Ende <hat|haben> {N} die meisten Kollegen überzeugt.
NS|scheitern|plan|*|Leider <ist|sind> {N} an den hohen Kosten gescheitert.
NS|gelingen|success|mfn|Zum Glück <ist|sind> {N} doch noch gelungen.
NP|sein|job|*|Das <ist|sind> {N} aus unserer Abteilung.
NP|sein|building|*|Das <ist|sind> {N} in der Innenstadt.
NP|sein|doc|*|Das <ist|sind> {N} von der Behörde.
NS|sein|doc|*|Wo <ist|sind> {N}?
NS|sein|mail|*|Wo <ist|sind> {N}?
NS|kosten|buy|*|Wie viel <kostet|kosten> {N}?
NS|gelten|rule|*|Seit wann <gilt|gelten> {N}?
NS|funktionieren|tech|*|Warum <funktioniert|funktionieren> {N} nicht?
NS|sein|bookable|*|<Ist|Sind> {N} noch verfügbar?
NS|beginnen|scheduled|*|Wann <beginnt|beginnen> {N}?
NS|zurückkommen|job|*|Wann <kommt|kommen> {N} zurück?
NS|sein|value|*|Warum <ist|sind> {N} so wichtig?
NS|abfahren|rail|*|Von Gleis drei <fährt|fahren> {N} ab.
NS|hängen|hang|*|An der Wand <hängt|hängen> {N}.

# ================= AKKUSATIV =================
AV|unterschreiben|sign|mfn|Bevor wir anfangen, muss ich noch {N} unterschreiben.
AV|einreichen|submit|mfn|Bis Freitag müssen Sie {N} beim Amt einreichen.
AV|ausfüllen|fill|mfn|Ich muss heute Abend noch {N} ausfüllen.
AV|beantragen|apply|mfn|Wo kann man {N} beantragen?
AV|verlängern|valid|mfn|Ich möchte {N} rechtzeitig verlängern lassen.
AV|kündigen|cancel|mfn|Zum Monatsende werde ich {N} kündigen.
AV|abschließen|conclude|mfn|Letzte Woche habe ich {N} erfolgreich abgeschlossen.
AV|bezahlen|pay|mfn|Ich habe {N} noch nicht bezahlt.
AV|überweisen|pay|mfn|Bitte überweisen Sie {N} bis zum Ersten des Monats.
AV|prüfen|check|mfn|Die Sachbearbeiterin prüft {N} sehr sorgfältig.
AV|erhalten|mail|mfn|Gestern habe ich endlich {N} erhalten.
AV|schicken|send|mfn|Ich schicke Ihnen {N} noch heute per E-Mail.
AV|schreiben|write|mfn|Bis morgen muss ich noch {N} schreiben.
AV|lesen|read|mfn|Ich habe {N} gestern Abend in Ruhe gelesen.
AV|vorbereiten|prep|mfn|Für Montag muss ich noch {N} vorbereiten.
AV|halten|giveTalk|mfn|Im Hörsaal hält die Professorin {N} vor vielen Studenten.
AV|besuchen|attend|mfn|Im nächsten Semester besuche ich {N}.
AV|bestehen|exam|mfn|Er hofft, {N} im ersten Versuch zu bestehen.
AV|wiederholen|study|mfn|Vor der Prüfung sollte man {N} noch einmal wiederholen.
AV|erklären|study|mfn|Kannst du mir {N} bitte noch einmal erklären?
AV|besprechen|topic|mfn|Wir besprechen {N} in der nächsten Sitzung.
AV|verschieben|scheduled|mfn|Können wir {N} auf nächste Woche verschieben?
AV|absagen|scheduled|mfn|Wegen der Krankheit mussten wir {N} leider absagen.
AV|vereinbaren|arrange|mfn|Ich möchte gern {N} vereinbaren.
AV|leiten|negotiation|mfn|Heute leitet der Chef {N} selbst.
AV|organisieren|orga|mfn|Unsere Abteilung organisiert {N} für alle Mitarbeiter.
AV|einstellen|hire|*|Die Firma stellt {N} im nächsten Monat ein.
AV|beraten|client|*|Der Berater berät {N} ausführlich zum Thema Versicherung.
AV|untersuchen|patient|*|Der Arzt untersucht {N} gründlich.
AV|behandeln|patient|*|Die Ärztin behandelt {N} schon seit Wochen.
AV|begrüßen|customer|*|Die Direktorin begrüßt {N} persönlich am Eingang.
AV|einladen|visit|*|Zur Hochzeit laden wir {N} natürlich auch ein.
AV|überzeugen|authority|*|Es gelang mir, {N} von meiner Idee zu überzeugen.
AV|unterstützen|visit|*|Wir unterstützen {N} finanziell.
AV|verstehen|feel|mfn|Ich kann {N} gut verstehen.
AV|akzeptieren|idea|mfn|Am Ende mussten wir {N} akzeptieren.
AV|akzeptieren|rule|mfn|Am Ende mussten wir {N} akzeptieren.
AV|ablehnen|idea|mfn|Der Ausschuss hat {N} leider abgelehnt.
AV|ablehnen|submit|mfn|Der Ausschuss hat {N} leider abgelehnt.
AV|diskutieren|topic|mfn|Im Seminar diskutieren wir {N}.
AV|kritisieren|policy|mfn|Die Opposition kritisiert {N} scharf.
AV|verabschieden|law|mfn|Das Parlament hat {N} verabschiedet.
AV|wählen|votable|*|Bei der Wahl haben viele Bürger {N} gewählt.
AV|unterstützen|fund|mfn|Die Stadt unterstützt {N} mit 50 000 Euro.
AV|planen|initiative|mfn|Die Firma plant {N} für nächstes Jahr.
AV|beginnen|starts|mfn|Nächste Woche beginne ich {N}.
AV|machen|dolong|mfn|Nach dem Abitur möchte ich {N} machen.
AV|verbessern|improve|mfn|Wir wollen {N} deutlich verbessern.
AV|lösen|solve|mfn|Gemeinsam haben wir {N} endlich gelöst.
AV|vermeiden|avoid|mfn|Wir sollten {N} unbedingt vermeiden.
AV|erreichen|achieve|mfn|Mit viel Fleiß hat sie {N} erreicht.
AV|erleben|experience|mfn|Im Urlaub habe ich {N} erlebt.
AV|verlieren|carry|mfn|Auf der Reise habe ich {N} verloren.
AV|vorzeigen|id|mfn|Am Eingang muss man {N} vorzeigen.
AV|kontrollieren|luggage|mfn|Am Flughafen kontrolliert der Zoll {N}.
AV|buchen|bookable|mfn|Ich habe {N} schon vor drei Monaten gebucht.
AV|stornieren|bookable|mfn|Leider mussten wir {N} kurzfristig stornieren.
AV|verpassen|transit|mfn|Wegen des Staus habe ich {N} verpasst.
AV|nehmen|transit|mfn|Ich nehme lieber {N}, weil es bequemer ist.
AV|besichtigen|sight|mfn|Am zweiten Tag besichtigen wir {N}.
AV|packen|luggage|mfn|Heute Abend muss ich noch {N} packen.
AV|mieten|rent|mfn|Wir mieten {N} für zwei Wochen.
AV|vermieten|viewing|mfn|Der Vermieter vermietet {N} nur an Studenten.
AV|renovieren|home|mfn|Im Sommer wollen wir {N} renovieren.
AV|besichtigen|viewing|mfn|Am Samstag besichtigen wir {N}.
AV|reparieren|tech|mfn|Der Techniker repariert {N} noch heute.
AV|installieren|software|mfn|Ich muss {N} auf dem neuen Laptop installieren.
AV|herunterladen|download|mfn|Bitte laden Sie {N} von der Homepage herunter.
AV|speichern|file|mfn|Vergiss nicht, {N} zu speichern.
AV|löschen|file|mfn|Versehentlich habe ich {N} gelöscht.
AV|ändern|change|mfn|Du solltest {N} regelmäßig ändern.
AV|kaufen|buy|mfn|Nach langem Überlegen haben wir {N} gekauft.
AV|bestellen|goods|mfn|Ich habe {N} gestern online bestellt.
AV|umtauschen|goods|mfn|Kann ich {N} umtauschen?
AV|liefern|goods|mfn|Die Firma liefert {N} innerhalb von drei Tagen.
AV|zurückschicken|goods|mfn|Ich habe {N} gestern zurückgeschickt.
AV|reklamieren|goods|mfn|Wir wollen {N} reklamieren.
AV|beobachten|trend|mfn|Journalisten beobachten {N} schon seit Monaten.
AV|verändern|society|mfn|Das Internet hat {N} stark verändert.
AV|schützen|nature|mfn|Wir müssen {N} besser schützen.
AV|reduzieren|reduce|mfn|Die Stadt will {N} in den nächsten Jahren deutlich reduzieren.
AV|melden|report|mfn|Bitte melden Sie {N} sofort der Versicherung.
AV|verursachen|damage|mfn|Der Sturm hat {N} verursacht.
AV|pflegen|visit|*|Sie pflegt {N} seit Jahren zu Hause.
AV|heiraten|partner|mfn|Nächsten Sommer heiratet mein Bruder {N}.
AV|kennenlernen|job|*|Auf der Konferenz habe ich {N} kennengelernt.
AV|überraschen|family|*|Wir wollen {N} mit einer Party überraschen.
AV|überraschen|friend|*|Wir wollen {N} mit einer Party überraschen.
AP|für|unit|mfn|Wir suchen ab sofort einen Mitarbeiter für {N}.
AP|ohne|entry|mfn|Ohne {N} kommt man nicht ins Gebäude.
AP|ohne|gadget|mfn|Ohne {N} kann ich heute nicht arbeiten.
AP|gegen|policy|mfn|Viele Bürger demonstrieren gegen {N}.
AP|gegen|illness|mfn|Der Arzt verschreibt ein Medikament gegen {N}.
AP|durch|throughable|mfn|Die Autobahn führt mitten durch {N}.
AP|durch|means|mfn|Er hat die Stelle durch {N} bekommen.
AP|schreiben über|topic|mfn|Der Journalist schreibt einen langen Artikel über {N}.
AP|sich bewerben um|position|mfn|Sie hat sich schon um {N} beworben.
AP|sich freuen auf|nice|mfn|Ich freue mich riesig auf {N}.
AP|sich vorbereiten auf|exam|mfn|Ich bereite mich intensiv auf {N} vor.
AP|sich vorbereiten auf|prep|mfn|Ich bereite mich intensiv auf {N} vor.
AP|sich konzentrieren auf|task|mfn|Ich muss mich jetzt ganz auf {N} konzentrieren.
AP|sich interessieren für|interest|mfn|Sie interessiert sich schon lange für {N}.
AP|sich entscheiden für|option|mfn|Am Ende haben wir uns für {N} entschieden.
AP|sich entscheiden gegen|option|mfn|Am Ende haben wir uns gegen {N} entschieden.
AP|verzichten auf|luxury|mfn|Aus Kostengründen verzichte ich auf {N}.
AP|achten auf|attention|mfn|Bitte achten Sie unbedingt auf {N}.
AP|sich erinnern an|memory|mfn|Ich erinnere mich gern an {N}.
AP|glauben an|hope|mfn|Trotz allem glaube ich an {N}.
AP|denken an|family|*|Ich denke oft an {N}.
AP|sich wenden an|contact|mfn|Bitte wenden Sie sich an {N}.
AP|sich handeln um|matter|mfn|Bei dem Schreiben handelt es sich um {N}.
AP|sich streiten über|dispute|mfn|Die Nachbarn streiten sich seit Wochen über {N}.
AP|sich ärgern über|annoy|mfn|Ich ärgere mich täglich über {N}.
AP|sich freuen über|pleasant|mfn|Wir haben uns sehr über {N} gefreut.
AP|verantwortlich für|responsible|mfn|Er ist für {N} verantwortlich.
AP|sorgen für|care|mfn|Wer sorgt in Zukunft für {N}?
AP|sich kümmern um|duty|mfn|Ich kümmere mich gern um {N}.
AW|in|into|mf|Morgen gehe ich noch schnell in {N}.
AW|auf|counter|mfn|Bitte legen Sie den Ausweis auf {N}.
AW|über|crossing|mfn|Die Straße führt direkt über {N}.
AW|unter|under|mfn|Ich lege den Schlüssel unter {N}.

# ================= DATIV =================
DV|helfen|student|*|Können Sie {N} bei der Bewerbung helfen?
DV|helfen|applicant|*|Können Sie {N} bei der Bewerbung helfen?
DV|danken|job|*|Ich möchte {N} herzlich für die Unterstützung danken.
DV|danken|group|*|Ich möchte {N} herzlich für die Unterstützung danken.
DV|gratulieren|student|*|Wir gratulieren {N} zur bestandenen Prüfung.
DV|antworten|client|*|Die Behörde hat {N} noch nicht geantwortet.
DV|zuhören|speaker|*|Alle hörten {N} aufmerksam zu.
DV|widersprechen|speaker|*|Nur wenige wagten es, {N} zu widersprechen.
DV|zustimmen|speaker|*|Die meisten Mitglieder stimmten {N} zu.
DV|zustimmen|agree|mfn|Alle Beteiligten stimmen {N} zu.
DV|folgen|guide|*|Bitte folgen Sie {N} zum Konferenzraum.
DV|gehören|owner|*|Das Grundstück gehört {N}.
DV|gefallen|adult|*|Der neue Vorschlag gefällt {N} überhaupt nicht.
DV|passen|adult|*|Der Termin passt {N} leider nicht.
DV|fehlen|applicant|*|Es fehlt {N} an Erfahrung.
DV|fehlen|student|*|Es fehlt {N} an Erfahrung.
DV|nützen|adult|*|Ein Sprachkurs nützt {N} auch im Beruf.
DV|glauben|adult|*|Ich glaube {N} kein Wort.
DV|misstrauen|authority|*|Viele Bürger misstrauen {N}.
DV|vertrauen|adult|*|Ich vertraue {N} vollkommen.
DV|drohen|employee|*|Der Chef drohte {N} mit der Kündigung.
DV|verzeihen|family|*|Ich habe {N} längst verziehen.
DV|verzeihen|friend|*|Ich habe {N} längst verziehen.
DV|ähneln|family|*|Er ähnelt {N} sehr.
DV|entsprechen|expect|mfn|Das Ergebnis entspricht {N} nicht.
DV|beitreten|club|*|Im Frühjahr ist sie {N} beigetreten.
DV|folgen|route|mfn|Folgen Sie {N} bis zur nächsten Kreuzung.
DV|ausweichen|obstacle|mfn|Der Fahrer wich {N} im letzten Moment aus.
DI|geben|employee|*|Der Chef hat {N} mehr Zeit gegeben.
DI|zeigen|client|*|Der Verkäufer zeigt {N} das neue Modell.
DI|erklären|client|*|Die Beraterin erklärt {N} den Vertrag ausführlich.
DI|schicken|client|*|Ich schicke {N} die Unterlagen per Post.
DI|schicken|applicant|*|Ich schicke {N} die Unterlagen per Post.
DI|empfehlen|client|*|Ich empfehle {N} dieses Hotel.
DI|empfehlen|friend|*|Ich empfehle {N} dieses Hotel.
DI|anbieten|client|*|Wir bieten {N} einen Rabatt von zehn Prozent an.
DI|verkaufen|friend|*|Ich habe {N} mein altes Auto verkauft.
DI|verkaufen|employee|*|Ich habe {N} mein altes Auto verkauft.
DI|vorlesen|child|*|Jeden Abend liest sie {N} eine Geschichte vor.
DI|beibringen|student|*|Er bringt {N} das Programmieren bei.
DI|mitteilen|client|*|Die Behörde teilt {N} das Ergebnis schriftlich mit.
DI|liefern|client|*|Wir liefern {N} die Ware kostenlos.
DI|schulden|friend|*|Er schuldet {N} noch zweihundert Euro.
DI|schulden|employee|*|Er schuldet {N} noch zweihundert Euro.
DI|leihen|friend|*|Kannst du {N} dein Auto leihen?
DI|leihen|partner|*|Kannst du {N} dein Auto leihen?
DP|mit|adult|*|Ich habe gestern lange mit {N} gesprochen.
DP|mit|job|*|Nächste Woche habe ich einen Termin mit {N}.
DP|umgehen mit|tool|mfn|Ich kann mit {N} leider nicht umgehen.
DP|mit|vehicle|mfn|Wir reisen lieber mit {N} als mit dem Auto.
DP|mit|payby|mfn|Kann ich hier mit {N} bezahlen?
DP|mit|difficult|mfn|Ich komme mit {N} nicht zurecht.
DP|mit|satisfy|mfn|Wir sind mit {N} sehr zufrieden.
DP|mit|topic|mfn|Ich beschäftige mich gerade mit {N}.
DP|mit|scheduled|mfn|Wir fangen gleich mit {N} an.
DP|mit|risk|mfn|Auf dieser Strecke muss man mit {N} rechnen.
DP|nach|after|mfn|Nach {N} gehe ich sofort nach Hause.
DP|nach|askabout|mfn|Ich habe bei der Rezeption nach {N} gefragt.
DP|nach|search|mfn|Wir suchen schon lange nach {N}.
DP|aus|origin|mfn|Sie kommt ursprünglich aus {N}.
DP|aus|container|mfn|Ich nehme das Formular aus {N}.
DP|seit|since|mfn|Ich warte seit {N} auf eine Antwort.
DP|von|adult|fp|Ich habe gestern eine Nachricht von {N} bekommen.
DP|zu|visit|p|Am Wochenende fahren wir zu {N}.
DP|zu|client|p|Der Vertreter kommt gerne zu {N} nach Hause.
DP|bei|employer|fp|Nach dem Studium arbeitet sie bei {N}.
DP|bei|visit|fp|Wir haben gestern bei {N} zu Abend gegessen.
DP|gegenüber|building|mfn|Das Büro liegt direkt gegenüber {N}.
DP|gemäß|terms|mfn|Gemäß {N} muss die Miete pünktlich bezahlt werden.
DP|außer|adult|*|Alle waren pünktlich da, außer {N}.
DP|teilnehmen an|scheduled|fp|Alle Mitarbeiter sollen an {N} teilnehmen.
DP|leiden an|health|fp|Er leidet schon lange an {N}.
DP|zweifeln an|doubt|fp|Ich zweifle ernsthaft an {N}.
DP|arbeiten an|worktask|fp|Wir arbeiten seit Monaten an {N}.
DP|handeln von|topic|fp|Der Bericht handelt von {N}.
DW|auf|counter|mfn|Der Ausweis liegt auf {N}.
DW|in|contains|fp|Das Dokument befindet sich in {N}.
DW|in|workplace|fp|Sie arbeitet seit drei Jahren in {N}.
DW|an|campus|f|Wir haben uns damals an {N} kennengelernt.
DW|an|wait_at|f|Wir warten schon lange an {N}.
DW|vor|building|mfn|Wir treffen uns morgen vor {N}.
DW|neben|building|mfn|Der Parkplatz liegt neben {N}.
DW|hinter|building|mfn|Hinter {N} gibt es einen kleinen Park.
DW|zwischen|building|mfn|Der Parkplatz liegt zwischen {N} und dem Fluss.
DW|über|shop|mfn|Ihre Wohnung liegt genau über {N}.
DW|unter|building|mfn|Die Tiefgarage befindet sich unter {N}.
DW|auf|list|mfn|Die Namen stehen auf {N}.
DW|an|wall|fp|Der Zettel hängt an {N}.

# ================= GENITIV =================
GP|wegen|cause|mfn|Wegen {N} wurde der Termin verschoben.
GP|trotz|cause|mfn|Trotz {N} kam er pünktlich zur Arbeit.
GP|trotz|difficulty|mfn|Trotz {N} haben sie das Projekt beendet.
GP|während|period|mfn|Während {N} bleibt das Büro geschlossen.
GP|während|show|mfn|Während {N} darf man nicht telefonieren.
GP|innerhalb|deadline|mfn|Innerhalb {N} müssen Sie den Antrag einreichen.
GP|außerhalb|region|mfn|Außerhalb {N} gelten andere Regeln.
GP|aufgrund|cause|mfn|Aufgrund {N} bleibt die Straße gesperrt.
GP|angesichts|crisis|mfn|Angesichts {N} müssen wir schnell handeln.
GP|infolge|cause|mfn|Infolge {N} kam es zu langen Verspätungen.
GP|statt|vehicle|mfn|Statt {N} bin ich diesmal zu Fuß gegangen.
GP|anhand|evidence|mfn|Anhand {N} kann man das Problem gut erkennen.
GP|mithilfe|tool|mfn|Mithilfe {N} haben wir den Fehler gefunden.
GP|bezüglich|matter2|mfn|Bezüglich {N} melde ich mich morgen bei Ihnen.
GP|hinsichtlich|topic|mfn|Hinsichtlich {N} gibt es noch offene Fragen.
GA|Ergebnis|assessed|mfn|Das Ergebnis {N} liegt schon vor.
GA|Termin|doctor|*|Der Termin {N} ist morgen um neun Uhr.
GA|Praxis|doctor|*|Die Praxis {N} liegt im Stadtzentrum.
GA|Meinung|adult|*|Ich kenne die Meinung {N} nicht.
GA|Vorschlag|adult|*|Der Vorschlag {N} hat uns überzeugt.
GA|Vorschlag|group|*|Der Vorschlag {N} hat uns überzeugt.
GA|Entscheidung|authority|*|Die Entscheidung {N} ist endgültig.
GA|Adresse|adult|*|Kannst du mir die Adresse {N} geben?
GA|Adresse|firm|mfn|Kannst du mir die Adresse {N} geben?
GA|Telefonnummer|adult|*|Ich habe die Telefonnummer {N} verloren.
GA|Öffnungszeiten|open|mfn|Wie sind die Öffnungszeiten {N}?
GA|Haupteingang|building|mfn|Der Haupteingang {N} ist gesperrt.
GA|Leiter|unit|mfn|Der Leiter {N} ist heute nicht im Haus.
GA|Gründung|unit|mfn|Die Gründung {N} liegt schon dreißig Jahre zurück.
GA|Mitarbeiter|unit|mfn|Die Mitarbeiter {N} sind mit ihrem Gehalt unzufrieden.
GA|Ursache|trouble|mfn|Wir kennen die Ursache {N} noch nicht.
GA|Folgen|trouble|mfn|Niemand kennt die Folgen {N}.
GA|Folgen|policy|mfn|Niemand kennt die Folgen {N}.
GA|Lösung|trouble|mfn|Wer findet die Lösung {N}?
GA|Ende|negotiation|mfn|Am Ende {N} stand ein Kompromiss.
GA|Beginn|scheduled|mfn|Der Beginn {N} wurde auf zehn Uhr verschoben.
GA|Dauer|process|mfn|Die Dauer {N} ist noch unklar.
GA|Höhe|price|mfn|Die Höhe {N} steht im Vertrag.
GA|Qualität|goods|mfn|Die Qualität {N} hat uns überzeugt.
GA|Preis|goods|mfn|Der Preis {N} ist deutlich gestiegen.
GA|Lieferung|goods|mfn|Die Lieferung {N} dauert drei Tage.
GA|Bedienung|gadget|mfn|Die Bedienung {N} ist ziemlich einfach.
GA|Bürgermeister|town|mfn|Der Bürgermeister {N} hat eine Rede gehalten.
GA|Rand|region|mfn|Am Rand {N} liegt ein großer See.
GA|Geschichte|populated|mfn|Die Geschichte {N} ist sehr interessant.
GA|Bevölkerung|populated|mfn|Die Bevölkerung {N} wächst schnell.
GA|Zentrum|centered|mfn|Im Zentrum {N} findet ein Markt statt.
GA|Ziel|initiative|mfn|Das Ziel {N} ist klar definiert.
GA|Kosten|initiative|mfn|Die Kosten {N} sind gestiegen.
GA|Verlauf|course|mfn|Der Verlauf {N} war völlig unerwartet.
GA|Teilnehmer|scheduled|mfn|Die Teilnehmer {N} erhalten ein Zertifikat.
GA|Besitzer|owned|mfn|Der Besitzer {N} wohnt im Ausland.
GA|Miete|rent|mfn|Die Miete {N} ist sehr hoch.
GA|Zustand|home|mfn|Der Zustand {N} ist schlecht.
GA|Wert|goods|mfn|Der Wert {N} hat stark abgenommen.
GA|Bedeutung|value|mfn|Die Bedeutung {N} wird oft unterschätzt.
GA|Rolle|roleholder|mfn|Die Rolle {N} hat sich in den letzten Jahren verändert.
GA|Zukunft|roleholder|mfn|Wir sprechen heute über die Zukunft {N}.
GA|Verantwortung|unit|mfn|Die Verantwortung {N} ist klar geregelt.
"""


# ======================================================================
#  Personal pronouns (1st / 2nd person) - see lex_a.py for the format.
# ======================================================================
PRON_FRAMES = """
AV|informieren|x|*|Der Chef informiert {N} über die Änderung.
AV|beraten|x|*|Die Beraterin berät {N} zum Thema Versicherung.
AV|einstellen|x|*|Die Firma stellt {N} im nächsten Monat ein.
AV|einladen|x|*|Der Direktor lädt {N} zum Vorstellungsgespräch ein.
AV|unterstützen|x|*|Mein Kollege unterstützt {N} bei dem Projekt.
AV|überzeugen|x|*|Der Vorschlag hat {N} sofort überzeugt.
AV|überraschen|x|*|Die Nachricht hat {N} völlig überrascht.
AV|begleiten|x|*|Ein Mitarbeiter begleitet {N} zum Ausgang.
AV|kontaktieren|x|*|Die Behörde kontaktiert {N} schriftlich.
AV|benachrichtigen|x|*|Das Amt benachrichtigt {N} per E-Mail.
AV|loben|x|*|Der Chef lobt {N} für die Präsentation.
AV|abholen|x|*|Der Vermieter holt {N} vom Bahnhof ab.
AV|vertreten|x|*|Ein Anwalt vertritt {N} vor Gericht.
AV|betreuen|x|*|Eine Kollegin betreut {N} während des Praktikums.
AV|prüfen|x|*|Der Arzt prüft {N} gründlich vor der Operation.
AV|verstehen|x|*|Der Kunde versteht {N} nicht.
AV|erreichen|x|*|Die Sachbearbeiterin erreicht {N} nicht telefonisch.
AV|empfehlen|x|*|Die Firma empfiehlt {N} als Berater.
AP|für|x|*|Die Firma sucht eine Lösung für {N}.
AP|ohne|x|*|Die Sitzung beginnt nicht ohne {N}.
AP|gegen|x|*|Niemand stimmt gegen {N}.
AP|sich wenden an|x|*|Der Kunde wendet sich direkt an {N}.
AP|sich verlassen auf|x|*|Das Team verlässt sich auf {N}.
AP|sich interessieren für|x|*|Der Journalist interessiert sich sehr für {N}.
AP|glauben an|x|*|Die Mannschaft glaubt an {N}.
AP|sich erinnern an|x|*|Meine Kollegen erinnern sich gern an {N}.
AP|warten auf|x|*|Die Bewerber warten seit Tagen auf {N}.
AP|denken an|x|*|Der Chef denkt bei dieser Entscheidung auch an {N}.
DV|helfen|x|*|Ein Kollege hilft {N} beim Umzug.
DV|danken|x|*|Die Firma dankt {N} für die Unterstützung.
DV|gratulieren|x|*|Der Professor gratuliert {N} zur bestandenen Prüfung.
DV|antworten|x|*|Die Behörde hat {N} noch nicht geantwortet.
DV|zustimmen|x|*|Der Ausschuss stimmt {N} zu.
DV|widersprechen|x|*|Niemand widerspricht {N}.
DV|zuhören|x|*|Alle hören {N} aufmerksam zu.
DV|gefallen|x|*|Das neue Büro gefällt {N} sehr.
DV|fehlen|x|*|Bei der Bewerbung fehlt {N} noch ein Zeugnis.
DV|nützen|x|*|Ein Sprachkurs nützt {N} im Beruf.
DV|vertrauen|x|*|Die Kunden vertrauen {N} vollkommen.
DV|drohen|x|*|Der Vermieter droht {N} mit einer Klage.
DV|folgen|x|*|Der Kollege folgt {N} zum Konferenzraum.
DV|gehören|x|*|Das Auto auf dem Parkplatz gehört {N}.
DI|geben|x|*|Der Chef gibt {N} mehr Zeit.
DI|zeigen|x|*|Der Verkäufer zeigt {N} das neue Modell.
DI|erklären|x|*|Die Beraterin erklärt {N} den Vertrag.
DI|schicken|x|*|Die Firma schickt {N} die Unterlagen per Post.
DI|empfehlen|x|*|Die Rezeption empfiehlt {N} ein gutes Restaurant.
DI|anbieten|x|*|Das Hotel bietet {N} ein Zimmer mit Balkon an.
DI|mitteilen|x|*|Die Behörde teilt {N} das Ergebnis schriftlich mit.
DI|liefern|x|*|Die Firma liefert {N} die Ware kostenlos.
DI|beibringen|x|*|Ein Kollege bringt {N} das Programmieren bei.
DI|verkaufen|x|*|Der Händler verkauft {N} ein gebrauchtes Auto.
DI|leihen|x|*|Meine Schwester leiht {N} ihr Auto.
DP|mit|x|*|Der Chef spricht morgen mit {N}.
DP|mit|x|*|Der Kunde ist mit {N} sehr zufrieden.
DP|zu|x|*|Der Vertreter kommt gerne zu {N} nach Hause.
DP|von|x|*|Die Nachricht ist von {N}.
DP|nach|x|*|Die Kollegin fragt nach {N}.
DP|bei|x|*|Die Kollegen sind heute bei {N} zum Essen.
DP|gegenüber|x|*|Der Chef sitzt im Büro {N} gegenüber.
DW|neben|x|*|Die Kollegin sitzt in der Besprechung neben {N}.
"""

PRON_PREDICATES = """
neu in der Firma
sehr beschäftigt
zum ersten Mal hier
gut vorbereitet
in Eile
ratlos
unzufrieden
zuversichtlich
verunsichert
spät dran
nervös
bereit
"""

PRON_DIALOGUES = """
ich|du|Hast du den Bericht schon gelesen? – Ja, {P} habe ihn gestern gelesen.|habe
ich|du|Kommst du zur Besprechung? – Ja, {P} komme um zehn.|komme
ich|du|Arbeitest du im Büro? – Nein, {P} arbeite im Homeoffice.|arbeite
ich|du|Studierst du noch? – Ja, {P} studiere im dritten Semester.|studiere
ich|du|Brauchst du das Formular? – Ja, {P} brauche es bis morgen.|brauche
ich|du|Hast du schon eine Wohnung? – Nein, {P} suche noch.|suche
ich|du|Fliegst du nach Berlin? – Nein, {P} nehme den Zug.|nehme
ich|du|Bewirbst du dich bei der Firma? – Ja, {P} bewerbe mich morgen.|bewerbe
ich|du|Kannst du mir den Vertrag erklären? – Ja, {P} erkläre ihn dir gern.|erkläre
ich|du|Hast du den Termin vergessen? – Nein, {P} bin schon unterwegs.|bin
ich|du|Sprichst du auch Englisch? – Ja, {P} spreche fließend Englisch.|spreche
ich|du|Bist du mit dem Ergebnis zufrieden? – Ja, {P} bin sehr zufrieden.|bin
ich|du|Machst du nächste Woche Urlaub? – Ja, {P} fahre nach Spanien.|fahre
ich|du|Schreibst du die Hausarbeit allein? – Nein, {P} schreibe sie mit einem Kollegen.|schreibe
ich|du|Hast du Zeit für ein Gespräch? – Ja, {P} habe jetzt Zeit.|habe
ich|du|Bereitest du dich auf die Prüfung vor? – Ja, {P} lerne jeden Abend.|lerne
ich|du|Fährst du zur Konferenz? – Ja, {P} fahre mit dem Zug.|fahre
wir|ihr|Habt ihr das Angebot geprüft? – Ja, {P} haben es heute Morgen geprüft.|haben
wir|ihr|Seid ihr mit dem Projekt fertig? – Nein, {P} sind noch nicht fertig.|sind
wir|ihr|Fahrt ihr zur Konferenz? – Ja, {P} fahren mit dem Zug.|fahren
wir|ihr|Arbeitet ihr zusammen? – Ja, {P} arbeiten seit Jahren im selben Team.|arbeiten
wir|ihr|Braucht ihr mehr Zeit? – Ja, {P} brauchen noch eine Woche.|brauchen
wir|ihr|Habt ihr den Vertrag unterschrieben? – Ja, {P} haben ihn gestern unterschrieben.|haben
wir|ihr|Bucht ihr das Hotel? – Ja, {P} buchen es heute noch.|buchen
wir|ihr|Sucht ihr eine neue Wohnung? – Ja, {P} suchen im Zentrum.|suchen
wir|ihr|Versteht ihr die Regel? – Ja, {P} verstehen sie jetzt.|verstehen
wir|ihr|Bereitet ihr euch vor? – Ja, {P} lernen jeden Tag.|lernen
wir|ihr|Kommt ihr zum Treffen? – Ja, {P} kommen pünktlich.|kommen
wir|ihr|Habt ihr schon einen Termin? – Ja, {P} haben nächsten Montag einen Termin.|haben
du|ich|Habe ich den Antrag richtig ausgefüllt? – Ja, {P} hast alles richtig gemacht.|hast
du|ich|Muss ich noch etwas unterschreiben? – Ja, {P} musst hier unterschreiben.|musst
du|ich|Kann ich später anrufen? – Ja, {P} kannst gern später anrufen.|kannst
du|ich|Bin ich für die Prüfung angemeldet? – Ja, {P} bist seit Montag angemeldet.|bist
du|ich|Soll ich die E-Mail schicken? – Ja, {P} solltest sie heute noch schicken.|solltest
du|ich|Habe ich einen Termin? – Ja, {P} hast morgen um neun einen Termin.|hast
du|ich|Darf ich das Fenster öffnen? – Ja, {P} darfst es öffnen.|darfst
du|ich|Muss ich die Rechnung bezahlen? – Ja, {P} musst sie bis Freitag bezahlen.|musst
du|ich|Bin ich zu früh? – Nein, {P} bist genau richtig.|bist
du|ich|Habe ich das Ergebnis richtig verstanden? – Ja, {P} hast es richtig verstanden.|hast
du|ich|Kann ich hier parken? – Ja, {P} kannst hier parken.|kannst
du|ich|Habe ich Post bekommen? – Ja, {P} hast einen Brief vom Amt bekommen.|hast
"""
