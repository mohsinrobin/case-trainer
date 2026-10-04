"""Verb + fixed preposition chunks.

One chunk per line:
  verb | preposition | case after it (Akk/Dat) | level (A/B/C) | English gloss | never-offer-as-distractor | note | sentence | sentence | ...

* In a sentence the preposition is written [like this] and the noun phrase that follows it {like this};
  the generator turns it into a blank and keeps the noun phrase for the explanation.
* "never-offer-as-distractor": prepositions that would ALSO be correct with this verb (comma separated).
  Prepositions of other chunks of the same verb are excluded automatically.
* "note": optional extra sentence for the explanation (contrast with similar verbs).
"""

CHUNKS = """
# ---------------------------------------------------------------- auf + Akk
warten|auf|Akk|A|to wait for|mit||Ich warte schon eine halbe Stunde [auf] {den Bus}.|Wir warten [auf] {die Antwort} der Firma.|Sie wartet [auf] {ihren Freund} vor dem Kino.
sich freuen|auf|Akk|A|to look forward to|über|sich freuen auf = looking forward to something in the future|Ich freue mich schon [auf] {den Urlaub} im Sommer.|Die Kinder freuen sich [auf] {das Wochenende}.|Wir freuen uns [auf] {deinen Besuch} nächste Woche.
aufpassen|auf|Akk|A|to look after, to watch out for|||Kannst du bitte [auf] {meinen Hund} aufpassen?|Die Eltern passen [auf] {die Kinder} auf.|Er passt [auf] {das Gepäck} auf.
hoffen|auf|Akk|B|to hope for|||Wir hoffen [auf] {besseres Wetter}.|Viele Menschen hoffen [auf] {eine Lösung} des Problems.|Er hofft [auf] {eine Antwort} bis Freitag.
sich verlassen|auf|Akk|B|to rely on|||Du kannst dich [auf] {mich} verlassen.|Die Mannschaft verlässt sich [auf] {ihren Torwart}.|Man kann sich nicht immer [auf] {den Wetterbericht} verlassen.
achten|auf|Akk|B|to pay attention to|||Bitte achten Sie [auf] {die Lautstärke}.|Er achtet sehr [auf] {gesunde Ernährung}.|Achte [auf] {die Zeit}, wir müssen pünktlich sein.
antworten|auf|Akk|B|to answer (a question, a mail)|||Ich muss noch [auf] {deine E-Mail} antworten.|Sie antwortet nie [auf] {meine Fragen}.|Er hat [auf] {die Einladung} nicht geantwortet.
reagieren|auf|Akk|B|to react to|nach||Wie hat er [auf] {die Nachricht} reagiert?|Die Firma reagiert schnell [auf] {Beschwerden}.|Sie reagierte [auf] {den Vorschlag} sehr positiv.
sich konzentrieren|auf|Akk|B|to concentrate on|||Ich kann mich heute nicht [auf] {die Arbeit} konzentrieren.|Konzentrier dich bitte [auf] {die Aufgabe}!|Die Schüler konzentrieren sich [auf] {die Prüfung}.
sich vorbereiten|auf|Akk|B|to prepare for|für||Ich bereite mich [auf] {das Gespräch} vor.|Wir bereiten uns [auf] {die Prüfung} vor.|Er bereitet sich [auf] {den Marathon} vor.
verzichten|auf|Akk|B|to do without, to give up|||Ich verzichte jetzt [auf] {Süßigkeiten}.|Viele verzichten [auf] {ein eigenes Auto}.|Wegen der Kosten verzichten wir [auf] {den Urlaub}.
ankommen|auf|Akk|B|to depend on (es kommt darauf an)|von||Es kommt [auf] {das Wetter} an.|Es kommt ganz [auf] {den Preis} an.|Es kommt [auf] {dich} an.
sich einigen|auf|Akk|B|to agree on|über|sich einigen auf = to reach an agreement on a result|Wir haben uns [auf] {einen Preis} geeinigt.|Die Partner einigten sich [auf] {einen Termin}.|Sie einigen sich [auf] {eine Lösung}.
anstoßen|auf|Akk|B|to drink a toast to|||Wir stoßen [auf] {das neue Jahr} an.|Sie stoßen [auf] {den Erfolg} an.|Lasst uns [auf] {deinen Geburtstag} anstoßen!
sich beziehen|auf|Akk|C|to refer to|||Ich beziehe mich [auf] {Ihre E-Mail} vom Montag.|Die Aussage bezieht sich [auf] {alle Mitarbeiter}.|Er bezieht sich [auf] {eine aktuelle Studie}.
hinweisen|auf|Akk|C|to point out|||Der Arzt weist [auf] {die Risiken} hin.|Ich möchte Sie [auf] {eine Änderung} hinweisen.|Das Schild weist [auf] {die Gefahr} hin.
bestehen|auf|Dat|B|to insist on|aus,in|bestehen auf = to insist on something (+ Dativ here)|Er besteht [auf] {seinem Recht}.|Sie besteht [auf] {einer schriftlichen Bestätigung}.|Der Kunde bestand [auf] {einem Umtausch}.
# ---------------------------------------------------------------- an + Akk
denken|an|Akk|A|to think of|über|denken an = to have someone or something in mind|Ich denke oft [an] {meine Familie}.|Er denkt [an] {den Termin} morgen.|Denk bitte [an] {deinen Schlüssel}!
glauben|an|Akk|B|to believe in|||Ich glaube [an] {das Gute} im Menschen.|Viele Menschen glauben [an] {Gott}.|Sie glaubt fest [an] {ihren Erfolg}.
sich erinnern|an|Akk|B|to remember|||Ich erinnere mich gern [an] {unseren Urlaub}.|Erinnerst du dich [an] {seinen Namen}?|Sie kann sich nicht [an] {den Unfall} erinnern.
sich gewöhnen|an|Akk|B|to get used to|||Ich gewöhne mich langsam [an] {das Klima}.|Die Kinder gewöhnen sich [an] {die neue Schule}.|Er muss sich [an] {den frühen Dienstbeginn} gewöhnen.
sich wenden|an|Akk|B|to turn to, to contact|gegen||Wenden Sie sich bitte [an] {den Kundenservice}.|Ich wende mich [an] {meinen Anwalt}.|Bei Fragen wenden Sie sich [an] {die Rezeption}.
erinnern|an|Akk|B|to remind of|||Das Foto erinnert mich [an] {unseren Urlaub}.|Die Melodie erinnert ihn [an] {seine Kindheit}.|Bitte erinnere mich [an] {den Termin}!
sich anpassen|an|Akk|C|to adapt to|||Er passt sich schnell [an] {die neue Umgebung} an.|Wir müssen uns [an] {die Situation} anpassen.|Das Unternehmen passt sich [an] {den Markt} an.
appellieren|an|Akk|C|to appeal to|||Der Minister appelliert [an] {die Vernunft} der Bürger.|Die Polizei appelliert [an] {die Autofahrer}.|Sie appellierte [an] {sein Gewissen}.
# ---------------------------------------------------------------- an + Dat
teilnehmen|an|Dat|B|to take part in|bei||Ich nehme [an] {einem Deutschkurs} teil.|Alle Mitarbeiter sollen [an] {der Schulung} teilnehmen.|Viele Schüler nehmen [an] {dem Wettbewerb} teil.
arbeiten|an|Dat|A|to work on|bei,für,mit,in||Er arbeitet [an] {einem neuen Projekt}.|Wir arbeiten [an] {der Lösung}.|Sie arbeitet seit Jahren [an] {ihrem Roman}.
leiden|an|Dat|B|to suffer from (an illness)|unter|leiden an = an illness; leiden unter = a situation|Er leidet [an] {einer schweren Krankheit}.|Viele Menschen leiden [an] {Diabetes}.|Sie leidet [an] {Asthma}.
zweifeln|an|Dat|B|to doubt|||Ich zweifle [an] {seiner Ehrlichkeit}.|Niemand zweifelt [an] {ihrem Können}.|Er zweifelt [an] {dem Erfolg} des Projekts.
sich beteiligen|an|Dat|B|to take part in, to contribute to|||Wir beteiligen uns [an] {der Aktion}.|Er beteiligt sich [an] {den Kosten}.|Viele Bürger beteiligen sich [an] {der Diskussion}.
liegen|an|Dat|B|to be due to|bei,in||Das liegt [an] {der Hitze}.|Es liegt nur [an] {deiner Einstellung}.|Es liegt [an] {dem schlechten Wetter}, dass wir zu spät sind.
sich orientieren|an|Dat|C|to take one's lead from|nach||Wir orientieren uns [an] {den Vorgaben} des Chefs.|Er orientiert sich [an] {seinen Vorbildern}.|Das Unternehmen orientiert sich [an] {den Kundenwünschen}.
erkranken|an|Dat|C|to fall ill with|||Er erkrankte [an] {einer Grippe}.|Viele erkrankten [an] {dem Virus}.|Sie ist [an] {Krebs} erkrankt.
mangeln|an|Dat|C|to lack|||Es mangelt [an] {Fachkräften}.|Es mangelt ihm [an] {Selbstvertrauen}.|Der Region mangelt es [an] {Wasser}.
# ---------------------------------------------------------------- über + Akk
sprechen|über|Akk|A|to talk about|mit,von|sprechen über = the topic; sprechen mit = the person|Wir sprechen oft [über] {das Wetter}.|Der Lehrer spricht [über] {die Prüfung}.|Ich möchte mit dir [über] {ein Problem} sprechen.
sich unterhalten|über|Akk|A|to chat about|mit,von||Wir unterhalten uns [über] {unseren Urlaub}.|Sie unterhalten sich [über] {die Arbeit}.|Die Frauen unterhalten sich [über] {das neue Café}.
sich freuen|über|Akk|A|to be pleased about|auf|sich freuen über = pleased about something that is here or has happened|Ich freue mich sehr [über] {dein Geschenk}.|Sie freut sich [über] {die gute Note}.|Wir freuen uns [über] {den Besuch} der Großeltern.
sich ärgern|über|Akk|A|to be annoyed about|||Ich ärgere mich [über] {den Lärm}.|Er ärgert sich [über] {die Verspätung}.|Sie ärgern sich [über] {die hohen Preise}.
lachen|über|Akk|A|to laugh at, to laugh about|mit||Alle lachen [über] {den Witz}.|Wir haben viel [über] {seinen Fehler} gelacht.|Sie lacht [über] {die Geschichte}.
nachdenken|über|Akk|B|to think about, to reflect on|an|nachdenken über = to reflect on something|Ich muss noch [über] {dein Angebot} nachdenken.|Sie denkt lange [über] {die Entscheidung} nach.|Wir denken [über] {einen Umzug} nach.
diskutieren|über|Akk|B|to discuss|mit,von,um||Wir diskutieren [über] {die neue Regel}.|Die Abgeordneten diskutieren [über] {das Gesetz}.|Sie diskutierten stundenlang [über] {Politik}.
sich beschweren|über|Akk|B|to complain about|bei|sich beschweren über = what you complain about; bei = to whom|Ich beschwere mich [über] {den schlechten Service}.|Die Gäste beschweren sich [über] {die Lautstärke}.|Er hat sich [über] {das Essen} beschwert.
sich wundern|über|Akk|B|to be surprised at|||Ich wundere mich [über] {sein Verhalten}.|Wir wundern uns [über] {die Absage}.|Sie wunderte sich [über] {das Ergebnis}.
berichten|über|Akk|B|to report on|von|berichten über = to report on a topic|Die Zeitung berichtet [über] {den Unfall}.|Er berichtet [über] {seine Reise}.|Sie berichten [über] {die Lage} im Land.
sich informieren|über|Akk|B|to find out about|||Ich informiere mich [über] {die Preise}.|Sie informiert sich [über] {den Studiengang}.|Man kann sich im Internet [über] {Angebote} informieren.
staunen|über|Akk|B|to marvel at|||Die Touristen staunen [über] {die Größe} der Kirche.|Wir staunten [über] {sein Wissen}.|Alle staunten [über] {den Erfolg}.
sich streiten|über|Akk|B|to argue about|bei,mit,um||Die Nachbarn streiten sich [über] {den Lärm}.|Wir streiten uns oft [über] {Kleinigkeiten}.|Sie streiten sich [über] {die Miete}.
entscheiden|über|Akk|C|to decide on (a matter)|für,gegen|entscheiden über = to rule on a matter; sich entscheiden für = to choose|Der Richter entscheidet [über] {den Fall}.|Der Ausschuss entscheidet [über] {den Antrag}.|Wer entscheidet [über] {die Vergabe} des Preises?
verfügen|über|Akk|C|to have at one's disposal|||Das Unternehmen verfügt [über] {große Erfahrung}.|Er verfügt [über] {ein gutes Gedächtnis}.|Die Stadt verfügt [über] {genug Geld}.
# ---------------------------------------------------------------- für + Akk
sich interessieren|für|Akk|A|to be interested in|an||Ich interessiere mich [für] {Musik}.|Er interessiert sich [für] {Fußball}.|Wir interessieren uns [für] {die Geschichte} der Stadt.
danken|für|Akk|A|to thank for|||Ich danke Ihnen [für] {die Einladung}.|Sie dankt ihm [für] {seine Hilfe}.|Wir danken euch [für] {das Geschenk}.
sich bedanken|für|Akk|A|to say thank you for|bei|sich bedanken für = what for; bedanken bei = whom|Ich bedanke mich [für] {das Geschenk}.|Er bedankt sich [für] {die Hilfe}.|Wir bedanken uns [für] {die Unterstützung}.
sich entscheiden|für|Akk|B|to decide in favour of, to choose|gegen,über||Ich habe mich [für] {das blaue Auto} entschieden.|Sie entscheidet sich [für] {ein Studium}.|Wir haben uns [für] {die Wohnung} entschieden.
sorgen|für|Akk|B|to provide for, to see to|um|sorgen für = to take care that something is there; sich sorgen um = to worry|Ich sorge [für] {das Essen}.|Die Eltern sorgen [für] {ihre Kinder}.|Wer sorgt [für] {die Musik}?
sich entschuldigen|für|Akk|B|to apologise for|bei,wegen|sich entschuldigen für = what for; bei = to whom|Ich entschuldige mich [für] {die Verspätung}.|Er entschuldigt sich [für] {sein Verhalten}.|Sie entschuldigte sich [für] {den Fehler}.
stimmen|für|Akk|B|to vote for|gegen||Viele haben [für] {den Vorschlag} gestimmt.|Sie stimmt [für] {die Änderung}.|Die Mehrheit stimmte [für] {das Gesetz}.
gelten|für|Akk|B|to apply to|über||Diese Regel gilt [für] {alle Mitarbeiter}.|Das gilt [für] {jeden Kunden}.|Die Preise gelten nur [für] {dieses Wochenende}.
halten|für|Akk|B|to consider, to take for|von|halten für = to consider something to be; halten von = to think of|Ich halte ihn [für] {einen guten Lehrer}.|Alle halten das [für] {eine gute Idee}.|Man hielt sie [für] {die Chefin}.
sich begeistern|für|Akk|B|to be enthusiastic about|an||Sie begeistert sich [für] {Kunst}.|Er begeistert sich [für] {die Berge}.|Die Kinder begeistern sich [für] {Dinosaurier}.
kämpfen|für|Akk|B|to fight for|gegen,um,mit||Die Mitarbeiter kämpfen [für] {bessere Löhne}.|Sie kämpft [für] {ihre Rechte}.|Viele Menschen kämpfen [für] {den Frieden}.
sich einsetzen|für|Akk|B|to stand up for|gegen||Er setzt sich [für] {den Umweltschutz} ein.|Sie setzt sich [für] {die Kinder} ein.|Wir setzen uns [für] {mehr Gerechtigkeit} ein.
sich eignen|für|Akk|C|to be suitable for|zu||Dieser Text eignet sich [für] {den Unterricht}.|Er eignet sich [für] {diese Stelle}.|Das Material eignet sich [für] {den Außenbereich}.
# ---------------------------------------------------------------- um + Akk
sich kümmern|um|Akk|A|to take care of|für||Ich kümmere mich [um] {die Kinder}.|Er kümmert sich [um] {den Garten}.|Wer kümmert sich [um] {das Essen}?
bitten|um|Akk|A|to ask for|||Ich bitte Sie [um] {Ihre Hilfe}.|Er bittet mich [um] {einen Gefallen}.|Sie bat [um] {ein Glas Wasser}.
sich bewerben|um|Akk|B|to apply for (a position)|bei,für,auf|sich bewerben um = the job; bei = the company|Er bewirbt sich [um] {die Stelle}.|Ich bewerbe mich [um] {ein Praktikum}.|Sie bewirbt sich [um] {einen Studienplatz}.
gehen|um|Akk|B|to be about (es geht um)|für,in,über||Es geht [um] {die Zukunft}.|Es geht [um] {viel Geld}.|In dem Film geht es [um] {eine große Liebe}.
sich sorgen|um|Akk|B|to worry about|für,über||Ich sorge mich [um] {meine Mutter}.|Sie sorgt sich [um] {die Zukunft} ihrer Kinder.|Wir sorgen uns [um] {dich}.
streiten|um|Akk|B|to fight over|für,mit,über||Die Geschwister streiten [um] {das Erbe}.|Sie streiten [um] {den letzten Platz}.|Die Parteien streiten [um] {die Macht}.
sich handeln|um|Akk|B|to be a case of|||Es handelt sich [um] {einen Irrtum}.|Bei dem Fund handelt es sich [um] {eine alte Münze}.|Es handelt sich [um] {ein wichtiges Dokument}.
beneiden|um|Akk|C|to envy (someone) for|für||Ich beneide dich [um] {deine Ruhe}.|Er beneidet sie [um] {ihr Talent}.|Alle beneiden ihn [um] {sein Glück}.
# ---------------------------------------------------------------- mit + Dat
sprechen|mit|Dat|A|to talk with|von,zu,über|sprechen mit = the person; sprechen über = the topic|Ich spreche gern [mit] {meiner Oma}.|Der Arzt spricht [mit] {dem Patienten}.|Kannst du bitte [mit] {dem Chef} sprechen?
telefonieren|mit|Dat|A|to phone|||Ich telefoniere jeden Tag [mit] {meiner Mutter}.|Er telefoniert [mit] {einem Kunden}.|Sie telefoniert gerade [mit] {ihrer Schwester}.
anfangen|mit|Dat|A|to begin with|bei,nach,vor||Wir fangen [mit] {dem Unterricht} an.|Fangt bitte [mit] {der ersten Aufgabe} an!|Er fängt [mit] {dem Training} an.
beginnen|mit|Dat|A|to begin with|bei,nach,vor||Wir beginnen [mit] {dem Frühstück}.|Er beginnt [mit] {der Arbeit} um acht.|Der Film beginnt [mit] {einer Szene} am Strand.
aufhören|mit|Dat|A|to stop (doing)|||Er hört [mit] {dem Rauchen} auf.|Hör bitte [mit] {dem Lärm} auf!|Wann hörst du [mit] {der Arbeit} auf?
sich treffen|mit|Dat|A|to meet (with)|bei||Ich treffe mich [mit] {meinen Freunden}.|Wir treffen uns [mit] {unserem Lehrer}.|Sie trifft sich [mit] {einer Kollegin}.
sich verabreden|mit|Dat|A|to arrange to meet|bei||Ich verabrede mich [mit] {meiner Freundin}.|Er hat sich [mit] {einem Kollegen} verabredet.|Sie verabreden sich [mit] {den Nachbarn} zum Grillen.
rechnen|mit|Dat|B|to expect, to reckon with|auf||Wir rechnen [mit] {starkem Regen}.|Ich rechne [mit] {deiner Hilfe}.|Man muss [mit] {Verspätungen} rechnen.
sich beschäftigen|mit|Dat|B|to deal with, to be busy with|||Er beschäftigt sich [mit] {Geschichte}.|Wir beschäftigen uns [mit] {diesem Thema}.|Sie beschäftigt sich gern [mit] {Tieren}.
zusammenarbeiten|mit|Dat|B|to cooperate with|an,bei||Wir arbeiten eng [mit] {der Universität} zusammen.|Er arbeitet [mit] {mehreren Firmen} zusammen.|Die Polizei arbeitet [mit] {den Behörden} zusammen.
umgehen|mit|Dat|B|to handle, to deal with|||Er kann gut [mit] {Kindern} umgehen.|Wie gehst du [mit] {Kritik} um?|Man muss vorsichtig [mit] {dem Feuer} umgehen.
vergleichen|mit|Dat|B|to compare with|||Vergleiche den Preis [mit] {dem Angebot} im Internet.|Er vergleicht sich ständig [mit] {anderen}.|Wir vergleichen das Ergebnis [mit] {dem Vorjahr}.
zurechtkommen|mit|Dat|B|to cope with|bei||Ich komme [mit] {dem neuen Computer} nicht zurecht.|Sie kommt gut [mit] {ihren Kollegen} zurecht.|Er kommt [mit] {dem Stress} schlecht zurecht.
übereinstimmen|mit|Dat|C|to agree with, to match|||Das stimmt nicht [mit] {den Tatsachen} überein.|Ich stimme [mit] {dir} überein.|Die Zahlen stimmen [mit] {der Statistik} überein.
# ---------------------------------------------------------------- von + Dat
träumen|von|Dat|A|to dream of|||Ich träume [von] {einem eigenen Haus}.|Sie träumt [von] {einer Reise} nach Japan.|Die Kinder träumen [von] {dem Urlaub}.
erzählen|von|Dat|A|to tell about|aus,über||Er erzählt [von] {seiner Reise}.|Oma erzählt [von] {früheren Zeiten}.|Sie erzählt gern [von] {ihrer Kindheit}.
hören|von|Dat|A|to hear from, to hear of|||Ich habe lange nichts [von] {dir} gehört.|Hast du schon [von] {dem Unfall} gehört?|Wir hören bald [von] {der Firma}.
sich verabschieden|von|Dat|A|to say goodbye to|||Ich verabschiede mich [von] {meinen Freunden}.|Er verabschiedet sich [von] {seiner Familie}.|Wir verabschieden uns [von] {den Gästen}.
abhängen|von|Dat|B|to depend on|||Das hängt [von] {dem Wetter} ab.|Der Preis hängt [von] {der Menge} ab.|Alles hängt [von] {deiner Entscheidung} ab.
halten|von|Dat|B|to think of (opinion)|für|halten von = what you think of something; halten für = to consider something to be|Was hältst du [von] {diesem Plan}?|Ich halte nicht viel [von] {seinen Ideen}.|Was halten Sie [von] {dem Vorschlag}?
sich erholen|von|Dat|B|to recover from|auf,bei,nach,vor||Ich erhole mich [von] {der Arbeit}.|Er erholt sich [von] {der Krankheit}.|Wir erholen uns [von] {der Reise}.
leben|von|Dat|B|to live on|mit||Er lebt [von] {seinem Gehalt}.|Viele Menschen leben [von] {der Landwirtschaft}.|Sie lebt [von] {einer kleinen Rente}.
sich trennen|von|Dat|B|to part from|||Sie hat sich [von] {ihrem Mann} getrennt.|Ich trenne mich ungern [von] {meinem alten Auto}.|Er trennt sich [von] {der Firma}.
profitieren|von|Dat|B|to benefit from|||Alle profitieren [von] {dieser Regelung}.|Er profitiert [von] {seiner Erfahrung}.|Die Kunden profitieren [von] {den niedrigen Preisen}.
handeln|von|Dat|B|to be about (a book, a film)|||Das Buch handelt [von] {einer Familie}.|Der Film handelt [von] {zwei Freunden}.|Die Geschichte handelt [von] {einem Hund}.
sich unterscheiden|von|Dat|B|to differ from|||Das unterscheidet sich [von] {dem Original}.|Die neue Version unterscheidet sich [von] {der alten}.|Die Sorten unterscheiden sich [von] {den anderen}.
ausgehen|von|Dat|C|to assume, to start from|aus,für||Wir gehen [von] {einem Zuwachs} aus.|Wir gehen [von] {einem Fehler} aus.|Man geht [von] {einer Einigung} aus.
# ---------------------------------------------------------------- zu + Dat
einladen|zu|Dat|A|to invite to|bei,nach||Ich lade dich [zu] {meiner Party} ein.|Sie laden uns [zu] {ihrer Hochzeit} ein.|Er lädt uns [zu] {dem Essen} ein.
gratulieren|zu|Dat|A|to congratulate on|||Ich gratuliere dir [zu] {deinem Geburtstag}.|Wir gratulieren Ihnen [zu] {Ihrer Prüfung}.|Alle gratulierten ihr [zu] {dem Erfolg}.
gehören|zu|Dat|B|to belong to, to be among|nach||Er gehört [zu] {den besten Spielern}.|Sie gehört [zu] {der Familie}.|Dieses Gebiet gehört [zu] {Bayern}.
beitragen|zu|Dat|B|to contribute to|||Das trägt [zu] {einer besseren Stimmung} bei.|Jeder kann [zu] {dem Erfolg} beitragen.|Sport trägt [zu] {guter Gesundheit} bei.
führen|zu|Dat|B|to lead to|||Das führt [zu] {Problemen}.|Der Weg führt [zu] {einem See}.|Seine Fehler führten [zu] {der Kündigung}.
passen|zu|Dat|B|to go with, to suit|||Die Schuhe passen [zu] {dem Kleid}.|Das passt gut [zu] {deinem Charakter}.|Der Wein passt [zu] {dem Fisch}.
raten|zu|Dat|B|to advise (in favour of)|||Der Arzt rät [zu] {einer Operation}.|Ich rate dir [zu] {mehr Geduld}.|Sie rät [zu] {einem Umzug}.
sich entschließen|zu|Dat|B|to decide on|||Er entschloss sich [zu] {einem Studium}.|Wir haben uns [zu] {einem Umzug} entschlossen.|Sie entschließt sich [zu] {einer Reise}.
überreden|zu|Dat|B|to persuade to|bei||Sie überredete mich [zu] {einem Spaziergang}.|Er hat uns [zu] {einem Kauf} überredet.|Wir überredeten ihn [zu] {der Teilnahme}.
zählen|zu|Dat|C|to count among|||Er zählt [zu] {den Besten}.|Das zählt [zu] {meinen Aufgaben}.|Die Stadt zählt [zu] {den schönsten Städten} Europas.
neigen|zu|Dat|C|to tend to|||Er neigt [zu] {Übertreibungen}.|Sie neigt [zu] {Wutausbrüchen}.|Manche neigen [zu] {Pessimismus}.
sich äußern|zu|Dat|C|to comment on|in,über||Der Minister äußerte sich [zu] {den Vorwürfen}.|Möchten Sie sich [zu] {dem Thema} äußern?|Sie hat sich nicht [zu] {der Frage} geäußert.
# ---------------------------------------------------------------- bei + Dat
helfen|bei|Dat|A|to help with|an,auf,in,mit,nach,vor||Ich helfe ihm [bei] {der Arbeit}.|Kannst du mir [bei] {den Hausaufgaben} helfen?|Sie hilft [bei] {dem Umzug}.
sich bedanken|bei|Dat|A|to thank (someone)|für|sich bedanken bei = whom you thank|Ich bedanke mich [bei] {meinen Gästen}.|Er bedankt sich [bei] {dem Team}.|Wir bedanken uns [bei] {allen Helfern}.
sich entschuldigen|bei|Dat|B|to apologise to|für|sich entschuldigen bei = whom you apologise to|Ich entschuldige mich [bei] {dir}.|Er entschuldigte sich [bei] {den Nachbarn}.|Sie entschuldigt sich [bei] {ihrer Lehrerin}.
sich bewerben|bei|Dat|B|to apply to (a company)|um|sich bewerben bei = the company; um = the position|Ich bewerbe mich [bei] {einer Bank}.|Sie bewirbt sich [bei] {der Stadt}.|Er hat sich [bei] {mehreren Firmen} beworben.
sich beschweren|bei|Dat|B|to complain to|über|sich beschweren bei = whom you complain to|Ich beschwere mich [bei] {dem Manager}.|Er beschwert sich [bei] {der Hotelleitung}.|Sie haben sich [bei] {dem Vermieter} beschwert.
sich erkundigen|bei|Dat|B|to ask (at, someone)|auf,in,nach|sich erkundigen bei = whom you ask|Ich erkundige mich [bei] {der Auskunft}.|Er erkundigt sich [bei] {dem Arzt}.|Wir erkundigen uns [bei] {dem Reisebüro}.
bleiben|bei|Dat|B|to stick to|||Er bleibt [bei] {seiner Meinung}.|Ich bleibe [bei] {meinem Plan}.|Sie bleibt [bei] {ihrer Entscheidung}.
# ---------------------------------------------------------------- nach + Dat
fragen|nach|Dat|A|to ask about, to ask for|um||Ich frage [nach] {dem Weg}.|Er fragt [nach] {dem Preis}.|Sie fragt [nach] {meiner Gesundheit}.
suchen|nach|Dat|A|to search for|||Wir suchen [nach] {einer Lösung}.|Er sucht [nach] {seinem Schlüssel}.|Die Polizei sucht [nach] {dem Täter}.
riechen|nach|Dat|A|to smell of|||Es riecht [nach] {frischem Brot}.|Die Küche riecht [nach] {Kaffee}.|Der Garten riecht [nach] {Rosen}.
schmecken|nach|Dat|A|to taste of|||Die Suppe schmeckt [nach] {Knoblauch}.|Es schmeckt [nach] {Zitrone}.|Der Tee schmeckt [nach] {Minze}.
sich erkundigen|nach|Dat|B|to inquire about|bei,in,zu|sich erkundigen nach = what you ask about; bei = whom you ask|Ich erkundige mich [nach] {den Öffnungszeiten}.|Er erkundigt sich [nach] {dem Preis}.|Sie erkundigt sich [nach] {meiner Gesundheit}.
sich sehnen|nach|Dat|B|to long for|||Ich sehne mich [nach] {Ruhe}.|Er sehnt sich [nach] {seiner Heimat}.|Sie sehnt sich [nach] {dem Sommer}.
greifen|nach|Dat|B|to reach for|zu||Er greift [nach] {dem Glas}.|Das Kind greift [nach] {dem Ball}.|Sie griff [nach] {ihrer Tasche}.
streben|nach|Dat|C|to strive for|||Er strebt [nach] {Erfolg}.|Viele streben [nach] {Anerkennung}.|Sie strebt [nach] {einer besseren Zukunft}.
verlangen|nach|Dat|C|to ask for, to demand|von||Er verlangte [nach] {dem Chef}.|Das Kind verlangt [nach] {seiner Mutter}.|Die Gäste verlangten [nach] {der Rechnung}.
# ---------------------------------------------------------------- aus + Dat
bestehen|aus|Dat|B|to consist of|auf,in|bestehen aus = to be made up of|Die Gruppe besteht [aus] {zehn Personen}.|Das Gericht besteht [aus] {Reis und Gemüse}.|Der Kurs besteht [aus] {vier Modulen}.
stammen|aus|Dat|B|to come from, to originate in|von||Er stammt [aus] {einer kleinen Stadt}.|Die Familie stammt [aus] {der Türkei}.|Das Wort stammt [aus] {dem Lateinischen}.
schließen|aus|Dat|C|to conclude from|||Ich schließe [aus] {seinen Worten}, dass er zufrieden ist.|Man kann [aus] {diesen Zahlen} nichts schließen.|Was schließt du [aus] {dem Ergebnis}?
# ---------------------------------------------------------------- vor + Dat
Angst haben|vor|Dat|A|to be afraid of|bei||Ich habe Angst [vor] {dem Hund}.|Sie hat Angst [vor] {der Prüfung}.|Die Kinder haben Angst [vor] {Gewittern}.
sich fürchten|vor|Dat|B|to be afraid of|bei||Ich fürchte mich [vor] {der Dunkelheit}.|Er fürchtet sich [vor] {dem Zahnarzt}.|Sie fürchten sich [vor] {der Zukunft}.
warnen|vor|Dat|B|to warn of|bei||Ich warne dich [vor] {dem Hund}.|Der Wetterdienst warnt [vor] {starkem Regen}.|Die Polizei warnt [vor] {Betrügern}.
fliehen|vor|Dat|B|to flee from|aus,nach||Viele fliehen [vor] {dem Krieg}.|Er floh [vor] {seinen Verfolgern}.|Die Tiere fliehen [vor] {dem Feuer}.
schützen|vor|Dat|B|to protect from|gegen||Der Schirm schützt dich [vor] {dem Regen}.|Impfungen schützen [vor] {Krankheiten}.|Die Mauer schützt [vor] {dem Wind}.
sich verstecken|vor|Dat|B|to hide from|bei,mit||Das Kind versteckt sich [vor] {dem Hund}.|Sie versteckt sich [vor] {ihren Gläubigern}.|Er versteckte sich [vor] {der Polizei}.
# ---------------------------------------------------------------- gegen + Akk
protestieren|gegen|Akk|B|to protest against|für||Die Bürger protestieren [gegen] {den Bau}.|Viele protestieren [gegen] {die Steuererhöhung}.|Die Schüler protestieren [gegen] {den Lehrplan}.
sich wehren|gegen|Akk|B|to defend oneself against|für||Sie wehrt sich [gegen] {die Vorwürfe}.|Wir wehren uns [gegen] {die Kündigung}.|Er wehrt sich [gegen] {den Angriff}.
demonstrieren|gegen|Akk|B|to demonstrate against|für||Tausende demonstrieren [gegen] {den Krieg}.|Sie demonstrieren [gegen] {die Politik}.|Viele demonstrierten [gegen] {die Schließung}.
impfen|gegen|Akk|B|to vaccinate against|||Man kann sich [gegen] {die Grippe} impfen lassen.|Er ließ sich [gegen] {Masern} impfen.|Kinder werden [gegen] {viele Krankheiten} geimpft.
kämpfen|gegen|Akk|B|to fight against|für,um,mit||Die Ärzte kämpfen [gegen] {die Krankheit}.|Wir kämpfen [gegen] {die Armut}.|Sie kämpft [gegen] {ihre Angst}.
stimmen|gegen|Akk|B|to vote against|für,über||Einige stimmten [gegen] {den Antrag}.|Er hat [gegen] {die Reform} gestimmt.|Wir stimmen [gegen] {den Plan}.
verstoßen|gegen|Akk|C|to violate|||Er verstieß [gegen] {das Gesetz}.|Das verstößt [gegen] {die Regeln}.|Die Firma hat [gegen] {die Vorschriften} verstoßen.
sprechen|gegen|Akk|C|to speak against, to count against|für,mit,von,über||Vieles spricht [gegen] {diesen Plan}.|Alle Fakten sprechen [gegen] {ihn}.|Das spricht [gegen] {eine Verlängerung}.
# ---------------------------------------------------------------- in + Akk / Dat
sich verlieben|in|Akk|A|to fall in love with|||Er hat sich [in] {eine Kollegin} verliebt.|Sie verliebt sich [in] {den Nachbarn}.|Ich habe mich [in] {diese Stadt} verliebt.
einsteigen|in|Akk|A|to get in, to get on|||Wir steigen [in] {den Bus} ein.|Bitte steigen Sie [in] {die U-Bahn} ein.|Sie stieg [in] {das Taxi} ein.
übersetzen|in|Akk|B|to translate into|auf||Sie übersetzt den Text [in] {die deutsche Sprache}.|Er hat das Buch [in] {drei Sprachen} übersetzt.|Bitte übersetzen Sie den Satz [in] {das Englische}.
sich einmischen|in|Akk|C|to interfere in|||Er mischt sich ständig [in] {meine Angelegenheiten} ein.|Misch dich nicht [in] {fremde Probleme} ein!|Die Eltern mischten sich [in] {den Streit} ein.
investieren|in|Akk|C|to invest in|||Die Firma investiert [in] {neue Maschinen}.|Er investiert [in] {Aktien}.|Die Stadt investiert [in] {den Ausbau} des Verkehrs.
bestehen|in|Dat|C|to consist in, to lie in|aus,auf|bestehen in = what the essence of something is|Die Aufgabe besteht [in] {der Betreuung} der Gäste.|Das Problem besteht [in] {dem Mangel} an Zeit.|Sein Beitrag besteht [in] {der Organisation}.
"""
