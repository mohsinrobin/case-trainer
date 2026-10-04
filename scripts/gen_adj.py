#!/usr/bin/env python3
"""Generate the adjective-ending section (src/data/adj.json).

The blank is the ending of the adjective ("den groß___ Hund" -> en).
Every sentence is built from a noun (with gender / plural / genitive), a determiner type
(weak = der-words, mixed = ein-words, strong = no article) and a frame that fixes the case.

Usage:  python3 scripts/gen_adj.py
"""
import json
import math
import os
import random
import re
import zlib
from collections import Counter, defaultdict

CASES = ["Nom", "Akk", "Dat", "Gen"]
CASE_FULL = {"Nom": "Nominativ", "Akk": "Akkusativ", "Dat": "Dativ", "Gen": "Genitiv"}
GENDERS = ["m", "f", "n", "pl"]
GENDER_FULL = {"m": "masculine", "f": "feminine", "n": "neuter", "pl": "plural"}
ARTICLE = {"m": "der", "f": "die", "n": "das", "pl": "die"}
OPTIONS = ["e", "em", "en", "er", "es"]

# ----------------------------------------------------------------------------- endings
WEAK = {"Nom": ["e", "e", "e", "en"], "Akk": ["en", "e", "e", "en"],
        "Dat": ["en"] * 4, "Gen": ["en"] * 4}
MIXED = {"Nom": ["er", "e", "es", "en"], "Akk": ["en", "e", "es", "en"],
         "Dat": ["en"] * 4, "Gen": ["en"] * 4}
STRONG = {"Nom": ["er", "e", "es", "e"], "Akk": ["en", "e", "es", "e"],
          "Dat": ["em", "er", "em", "en"], "Gen": ["en", "er", "en", "er"]}
ENDINGS = {"weak": WEAK, "mixed": MIXED, "strong": STRONG}

DEF = {"Nom": ["der", "die", "das", "die"], "Akk": ["den", "die", "das", "die"],
       "Dat": ["dem", "der", "dem", "den"], "Gen": ["des", "der", "des", "der"]}
DIES = {"Nom": ["dieser", "diese", "dieses", "diese"], "Akk": ["diesen", "diese", "dieses", "diese"],
        "Dat": ["diesem", "dieser", "diesem", "diesen"], "Gen": ["dieses", "dieser", "dieses", "dieser"]}
JED = {"Nom": ["jeder", "jede", "jedes", None], "Akk": ["jeden", "jede", "jedes", None],
       "Dat": ["jedem", "jeder", "jedem", None], "Gen": ["jedes", "jeder", "jedes", None]}
EIN_END = {"Nom": ["", "e", "", "e"], "Akk": ["en", "e", "", "e"],
           "Dat": ["em", "er", "em", "en"], "Gen": ["es", "er", "es", "er"]}
EIN_STEMS = ["ein", "kein", "mein", "dein", "sein", "ihr", "unser"]


def determiners(decl, case, g):
    """All determiners that can stand in this cell, as (form, stem). Stem '' = no article."""
    if decl == "strong":
        return [("", "")]
    gi = GENDERS.index(g)
    if decl == "weak":
        return [(DEF[case][gi], "def")] * 3 + [(DIES[case][gi], "dies")]
    end = EIN_END[case][gi]
    return [(st + end, st) for st in EIN_STEMS if not (st == "ein" and g == "pl")]


# ----------------------------------------------------------------------------- adjectives
AG = {
    "fruit": "frisch lecker süß gesund billig günstig reif",
    "bread": "frisch lecker warm weich billig günstig",
    "sweet": "lecker süß frisch billig günstig",
    "hot": "frisch lecker warm heiß kalt gesund billig günstig scharf",
    "produce": "frisch lecker gesund billig günstig",
    "topping": "frisch lecker billig günstig",
    "hotdrink": "heiß warm kalt frisch stark lecker bitter süß",
    "colddrink": "kalt frisch lecker süß billig günstig",
    "adult": "freundlich nett klug fleißig ehrlich höflich lustig ruhig jung alt",
    "child": "klein jung nett lustig klug fleißig laut ruhig freundlich",
    "animal": "klein groß süß schnell faul laut jung alt freundlich schwarz weiß braun",
    "thing": "neu alt praktisch modern schwer leicht billig günstig wichtig schön hässlich gut schlecht",
    "clothing": "neu alt modern bequem schön hässlich rot blau grün schwarz weiß braun warm günstig praktisch",
    "veh": "neu alt schnell langsam modern bequem sauber schmutzig schwarz rot blau weiß groß klein praktisch",
    "table": "neu alt groß klein modern schön hässlich braun schwarz",
    "seat": "neu alt groß klein modern bequem weich schön hässlich",
    "town": "groß klein alt neu schön ruhig sauber laut",
    "building": "groß klein alt neu schön modern ruhig sauber hell laut",
    "home": "groß klein alt neu schön modern gemütlich ruhig sauber hell",
    "read": "neu alt interessant spannend lustig lang kurz gut schlecht wichtig",
    "film": "neu alt interessant spannend lustig lang kurz gut schlecht langweilig",
    "idea": "gut schlecht neu interessant wichtig einfach schwer lustig",
}

# sg | gender | plural | genitive | tags | adjective list (key or words) | flags
#   flags: mass = singular only, no "ein"      sg = singular only      n = n-declension (Kollege -> den Kollegen)
NOUNS = """
Mann|m|Männer|Mannes|person|adult|
Frau|f|Frauen|-|person|adult|
Freund|m|Freunde|Freundes|person|adult|
Freundin|f|Freundinnen|-|person|adult|
Lehrer|m|Lehrer|Lehrers|person|adult|
Lehrerin|f|Lehrerinnen|-|person|adult|
Nachbar|m|Nachbarn|Nachbarn|person|adult|n
Nachbarin|f|Nachbarinnen|-|person|adult|
Kollege|m|Kollegen|Kollegen|person|adult|n
Kollegin|f|Kolleginnen|-|person|adult|
Student|m|Studenten|Studenten|person|adult|n
Studentin|f|Studentinnen|-|person|adult|
Arzt|m|Ärzte|Arztes|person|adult|
Ärztin|f|Ärztinnen|-|person|adult|
Chef|m|Chefs|Chefs|person|adult|
Gast|m|Gäste|Gastes|person|adult|
Kind|n|Kinder|Kindes|person,play|child|
Mädchen|n|Mädchen|Mädchens|person,play|child|
Sohn|m|Söhne|Sohnes|person,play|klein jung nett klug fleißig lustig ruhig|
Tochter|f|Töchter|-|person,play|klein jung nett klug fleißig lustig ruhig|
Hund|m|Hunde|Hundes|animal,play|animal|
Katze|f|Katzen|-|animal,play|animal|
Pferd|n|Pferde|Pferdes|animal|animal|
Vogel|m|Vögel|Vogels|animal|animal|
Kuh|f|Kühe|-|animal|animal|
Schaf|n|Schafe|Schafes|animal|animal|
Apfel|m|Äpfel|Apfels|eat,buy,healthy|fruit|
Banane|f|Bananen|-|eat,buy,healthy|fruit|
Orange|f|Orangen|-|eat,buy,healthy|fruit|
Birne|f|Birnen|-|eat,buy,healthy|fruit|
Tomate|f|Tomaten|-|eat,buy,healthy,topping,cook|fruit|
Kartoffel|f|Kartoffeln|-|eat,buy,cook|produce|
Ei|n|Eier|Eies|eat,buy,topping,cook|produce|
Brot|n|-|Brotes|eat,buy|bread|mass
Brötchen|n|Brötchen|Brötchens|eat,buy|bread|
Kuchen|m|-|Kuchens|eat,buy|sweet|sg
Schokolade|f|-|-|eat,buy|sweet|mass
Eis|n|-|Eises|eat,buy|kalt lecker süß frisch billig günstig|mass
Suppe|f|-|-|eat,buy|hot|sg
Pizza|f|-|-|eat,buy|hot|sg
Salat|m|-|Salats|eat,buy,healthy|produce|sg
Fisch|m|-|Fisches|eat,buy,healthy|produce|mass
Fleisch|n|-|Fleisches|eat,buy,cook|produce|mass
Gemüse|n|-|Gemüses|eat,buy,healthy,cook|produce|mass
Obst|n|-|Obstes|eat,buy,healthy,cook|produce|mass
Reis|m|-|Reises|eat,buy,cook|hot|mass
Käse|m|-|Käses|eat,buy,topping,cook|topping|mass
Butter|f|-|-|buy,topping,cook|topping|mass
Honig|m|-|Honigs|buy,topping,addin|frisch süß lecker billig günstig|mass
Marmelade|f|-|-|buy,topping|sweet|mass
Schinken|m|-|Schinkens|eat,buy,topping|topping|mass
Kaffee|m|-|Kaffees|drink,buy|hotdrink|mass
Tee|m|-|Tees|drink,buy|hotdrink|mass
Wein|m|-|Weines|drink,buy,cook|colddrink|mass
Saft|m|-|Saftes|drink,buy,healthy|colddrink|mass
Bier|n|-|Bieres|drink,buy|kalt frisch lecker billig günstig|mass
Wasser|n|-|Wassers|drink,buy,cook,healthy|kalt warm frisch gut|mass
Milch|f|-|-|drink,buy,cook,addin,healthy|kalt warm frisch gesund lecker billig günstig|mass
Limonade|f|-|-|drink,buy|colddrink|mass
Öl|n|-|Öls|buy,cook|frisch gut billig günstig|mass
Zucker|m|-|Zuckers|buy,addin|weiß braun billig günstig|mass
Sahne|f|-|-|buy,addin|frisch kalt süß lecker|mass
Handy|n|Handys|Handys|buy,need,small,repair,search|thing|
Computer|m|Computer|Computers|buy,need,small,repair,search|thing|
Uhr|f|Uhren|-|buy,need,small,repair,search,wear|thing|
Lampe|f|Lampen|-|buy,need,small,repair,search|thing|
Brille|f|Brillen|-|buy,need,small,repair,search,wear|thing|
Kamera|f|Kameras|-|buy,need,small,repair,search|thing|
Foto|n|Fotos|Fotos|small|neu alt schön hässlich gut schlecht klein groß|
Schlüssel|m|Schlüssel|Schlüssels|need,small,search|neu alt klein groß wichtig|
Schirm|m|Schirme|Schirmes|buy,need,small,search|neu alt groß klein schwarz blau praktisch|
Tasche|f|Taschen|-|buy,need,small,search,container|neu alt groß klein schwer leicht schwarz braun rot praktisch modern|
Buch|n|Bücher|Buches|buy,need,small,read|read|
Zeitung|f|Zeitungen|-|buy,small,read|read|
Brief|m|Briefe|Briefes|small,read|read|
Geschichte|f|Geschichten|-|read|read|
Lied|n|Lieder|Liedes|song|neu alt schön gut schlecht laut ruhig lustig langsam schnell|
Musik|f|-|-|song|neu alt schön gut schlecht laut ruhig lustig|mass
Film|m|Filme|Filmes|watch,event,film|film|
Idee|f|Ideen|-|idea|idea|
Jacke|f|Jacken|-|buy,need,small,search,wear,container|clothing|
Hose|f|Hosen|-|buy,need,small,search,wear,container|clothing|
Mantel|m|Mäntel|Mantels|buy,need,small,search,wear|clothing|
Pullover|m|Pullover|Pullovers|buy,need,small,search,wear|clothing|
Hemd|n|Hemden|Hemdes|buy,need,small,search,wear|clothing|
Kleid|n|Kleider|Kleides|buy,need,small,search,wear|clothing|
Mütze|f|Mützen|-|buy,need,small,search,wear|clothing|
Auto|n|Autos|Autos|veh,buy,need,repair,search,park|veh|
Fahrrad|n|Fahrräder|Fahrrades|veh,buy,need,repair,search,park|veh|
Bus|m|Busse|-|veh,park,wait|veh|
Zug|m|Züge|-|veh,wait|veh|
Taxi|n|Taxis|-|veh,park,wait|veh|
Straßenbahn|f|Straßenbahnen|-|veh,wait|veh|
Tisch|m|Tische|-|furn,buy,need,search|table|
Regal|n|Regale|-|furn,buy,need,search|table|
Schrank|m|Schränke|-|furn,buy,need,search|table|
Stuhl|m|Stühle|-|furn,seat,buy,need,search|seat|
Sofa|n|Sofas|-|furn,seat,buy,need,search|seat|
Bett|n|Betten|-|furn,seat,buy,need,search|seat|
Stadt|f|Städte|-|visit,pass,live|town|
Dorf|n|Dörfer|-|visit,pass,live|town|
Straße|f|Straßen|-|pass,live|town|
Park|m|Parks|-|visit,pass,dest,work,place|town|
Haus|n|Häuser|Hauses|live,search,buy,need,dest|home|
Wohnung|f|Wohnungen|-|live,search,buy,need|home|
Zimmer|n|Zimmer|Zimmers|live,search,dest|home|
Küche|f|Küchen|-|dest,work|home|
Garten|m|Gärten|-|dest,work,search|home|
Büro|n|Büros|-|dest,work,comefrom,place|building|
Café|n|Cafés|-|dest,work,comefrom,visit,place|building|
Restaurant|n|Restaurants|-|dest,work,comefrom,visit,place|building|
Schule|f|Schulen|-|dest,work,comefrom,place|building|
Bibliothek|f|Bibliotheken|-|dest,work,comefrom,place|building|
Supermarkt|m|Supermärkte|-|dest,work,comefrom,place|building|
Hotel|n|Hotels|-|dest,work,comefrom,visit,place|building|
Kino|n|Kinos|-|dest,comefrom,place|building|
Museum|n|Museen|-|dest,visit,place|building|
Sommer|m|Sommer|Sommers|season,time|heiß warm lang kurz schön kalt|
Winter|m|Winter|Winters|season,time|kalt lang kurz schön warm|
Jahr|n|Jahre|Jahres|time|lang kurz anstrengend schön|
Woche|f|Wochen|-|time|lang kurz schön gut schlecht anstrengend|
Nacht|f|Nächte|-|time|lang kurz kalt ruhig schlecht gut laut|
Reise|f|Reisen|-|time,event|lang kurz schön anstrengend interessant spannend|
Arbeit|f|-|-|event|lang schwer anstrengend gut schlecht|sg
Pause|f|Pausen|-|event|lang kurz schön gut|
Party|f|Partys|-|event|lang kurz lustig laut schön gut|
Prüfung|f|Prüfungen|-|event|lang kurz schwer leicht wichtig anstrengend|
Konzert|n|Konzerte|Konzertes|event|lang kurz schön laut gut interessant|
Unterricht|m|-|Unterrichts|event|lang kurz interessant langweilig anstrengend gut|sg
Wetter|n|-|Wetters|wx|schlecht gut schön kalt warm heiß|mass
Regen|m|-|Regens|wx|stark leicht lang kalt|mass
Schnee|m|-|Schnees|wx|stark leicht kalt|mass
Wind|m|-|Windes|wx|stark leicht kalt warm|mass
Hitze|f|-|-|wx|groß stark|mass
Kälte|f|-|-|wx|groß stark|mass
Stau|m|Staus|Staus|cause|lang groß stark|
Baustelle|f|Baustellen|-|cause|groß lang|
Unfall|m|Unfälle|Unfalls|cause|schwer groß schlimm|
Krankheit|f|Krankheiten|-|cause|lang schwer schlimm|
Problem|n|Probleme|Problems|cause|groß schwer technisch|
"""


class Noun:
    def __init__(self, line):
        f = line.split("|")
        self.sg, self.g, pl, gen, tags, adj, flags = f
        self.pl = None if pl == "-" else pl
        self.gen = None if gen == "-" else gen
        self.tags = set(tags.split(","))
        self.adj = AG[adj].split() if adj in AG else adj.split()
        self.mass = "mass" in flags
        self.sgonly = self.mass or "sg" in flags
        self.ndecl = "n" in flags
        if self.g == "f":
            self.gen = self.sg
        if self.sgonly:
            assert self.pl is None, self.sg
        else:
            assert self.pl, self.sg

    def form(self, case, g):
        if g == "pl":
            if case == "Dat" and not self.pl.endswith(("n", "s")):
                return self.pl + "n"
            return self.pl
        if case == "Nom":
            return self.sg
        if case == "Gen":
            assert self.gen, f"genitive of {self.sg} missing"
            return self.gen
        if self.ndecl:
            return self.gen
        return self.sg


NOUN_LIST = [Noun(l) for l in NOUNS.strip().splitlines()]
EXTRA_TAGS = {
    "carry": "Handy Uhr Brille Schirm Schlüssel Tasche Kamera",
    "lunch": "Suppe Pizza Salat Fisch Fleisch Reis Gemüse Kartoffel",
    "breakfast": "Kaffee Tee Saft Milch Wasser",
    "order": "Kaffee Tee Saft Wasser Milch Limonade Kuchen Eis Salat Suppe",
    "walk": "Hund Pferd",
    "owner": "Mann Frau Freund Freundin Lehrer Lehrerin Nachbar Nachbarin Kollege Kollegin Student Studentin Arzt Ärztin Chef Gast",
}
# possessives only for things a person can own (not food, weather, public places, birds, ...)
NO_POSS_NAMES = set("Mädchen Vogel Kuh Schaf Taxi Bus Zug Straßenbahn Stadt Dorf Park Straße Museum Café Restaurant Hotel Kino Supermarkt Bibliothek Sommer Winter".split())
NO_POSS_TAGS = {"eat", "drink", "topping", "addin", "cook", "wx"}
NOPOSS = {"Mann": ("sein",), "Frau": ("ihr",)}   # "seinem Mann" / "ihrer Frau" read as a married couple
for _n in NOUN_LIST:
    for _t, _words in EXTRA_TAGS.items():
        if _n.sg in _words.split():
            _n.tags.add(_t)
    _n.noposs = NOPOSS.get(_n.sg, ())
    _n.no_poss_at_all = _n.sg in NO_POSS_NAMES or bool(_n.tags & NO_POSS_TAGS)
assert len({n.sg for n in NOUN_LIST}) == len(NOUN_LIST)

# ----------------------------------------------------------------------------- frames
# case | template | noun tags (any) | why this case | mode   (s = singular only, x = also without article)
# "{a/b}" = verb form for singular | plural subject
SMALL_LIKE = "small clothing veh place film song idea furn read"
FRAMES = """
Nom|{NP} {wartet/warten} vor der Tür.|person|it is the subject of the sentence (who waits?) → Nominativ|
Nom|{NP} {kommt/kommen} heute zur Party.|person|it is the subject of the sentence (who comes?) → Nominativ|
Nom|{NP} {hilft/helfen} uns oft.|person|it is the subject of the sentence (who helps?) → Nominativ|x
Nom|{NP} {schläft/schlafen} im Garten.|animal|it is the subject of the sentence (who sleeps?) → Nominativ|
Nom|{NP} {spielt/spielen} im Park.|play|it is the subject of the sentence (who plays?) → Nominativ|x
Nom|{NP} {liegt/liegen} auf dem Tisch.|small|it is the subject of the sentence (what lies there?) → Nominativ|x
Nom|{NP} {gefällt/gefallen} mir sehr.|SMALL_LIKE|it is the subject of the sentence (what pleases me?) → Nominativ|x
Nom|{NP} {schmeckt/schmecken} wirklich gut.|eat drink|it is the subject of the sentence (what tastes good?) → Nominativ|x
Nom|{NP} {ist/sind} heute im Angebot.|eat drink small clothing|it is the subject of the sentence (what is on offer?) → Nominativ|x
Nom|{NP} {ist/sind} gesund.|healthy|it is the subject of the sentence (what is healthy?) → Nominativ|x
Nom|{NP} {kommt/kommen} bald.|wx season|it is the subject of the sentence (what is coming?) → Nominativ|x
Nom|{NP} {bleibt/bleiben} zum Glück nicht lange.|wx|it is the subject of the sentence (what does not stay?) → Nominativ|x
Nom|{NP} {liegt/liegen} direkt im Zentrum.|place|it is the subject of the sentence (what lies there?) → Nominativ|x
Nom|{NP} {steht/stehen} vor dem Haus.|park|it is the subject of the sentence (what stands there?) → Nominativ|x
Nom|{NP} {beginnt/beginnen} um acht Uhr.|event|it is the subject of the sentence (what begins?) → Nominativ|
Akk|Ich kaufe {NP}.|buy|'kaufen' takes a direct object (what do I buy?) → Akkusativ|x
Akk|Zum Mittagessen esse ich {NP}.|lunch|'essen' takes a direct object (what do I eat?) → Akkusativ|x
Akk|Zum Frühstück trinke ich {NP}.|breakfast|'trinken' takes a direct object (what do I drink?) → Akkusativ|x
Akk|Im Café bestelle ich {NP}.|order|'bestellen' takes a direct object (what do I order?) → Akkusativ|x
Akk|Ich kenne {NP} schon lange.|person|'kennen' takes a direct object (whom do I know?) → Akkusativ|x
Akk|Wir besuchen {NP} am Sonntag.|person|'besuchen' takes a direct object (whom do we visit?) → Akkusativ|x
Akk|Im Zoo sehen wir {NP}.|animal|'sehen' takes a direct object (whom do we see?) → Akkusativ|x
Akk|Wir füttern {NP} jeden Tag.|animal|'füttern' takes a direct object (whom do we feed?) → Akkusativ|x
Akk|Ich brauche {NP}.|need|'brauchen' takes a direct object (what do I need?) → Akkusativ|x
Akk|Ich suche {NP}.|search|'suchen' takes a direct object (what am I looking for?) → Akkusativ|x
Akk|Er repariert {NP} heute.|repair|'reparieren' takes a direct object (what does he repair?) → Akkusativ|x
Akk|Heute trage ich {NP}.|wear|'tragen' takes a direct object (what do I wear?) → Akkusativ|x
Akk|Wir besuchen {NP} am Wochenende.|visit|'besuchen' takes a direct object (what do we visit?) → Akkusativ|x
Akk|Abends lese ich {NP}.|read|'lesen' takes a direct object (what do I read?) → Akkusativ|x
Akk|Am Abend sehen wir {NP}.|watch|'sehen' takes a direct object (what do we watch?) → Akkusativ|x
Akk|Ich höre {NP} im Auto.|song|'hören' takes a direct object (what do I listen to?) → Akkusativ|x
Akk|Das ist ein Geschenk für {NP}.|person|'für' always takes the Akkusativ|x
Akk|Ich gehe nie ohne {NP} aus dem Haus.|carry|'ohne' always takes the Akkusativ|s
Akk|Wir gehen durch {NP}.|pass|'durch' always takes the Akkusativ|s
Akk|Ich gehe in {NP}.|dest|'in' + movement (wohin? where to?) → Akkusativ|s
Akk|Er legt das Buch auf {NP}.|furn|'auf' + movement (wohin? where to?) → Akkusativ|s
Akk|Ich denke oft an {NP}.|person|'denken an' takes the Akkusativ|x
Akk|Er wartet auf {NP}.|person wait|'warten auf' takes the Akkusativ|x
Dat|Ich wohne in {NP}.|live|'in' + place (wo? where?) → Dativ|s
Dat|Er arbeitet in {NP}.|work|'in' + place (wo? where?) → Dativ|s
Dat|Das Buch liegt auf {NP}.|furn|'auf' + place (wo? where?) → Dativ|s
Dat|Ich sitze gern auf {NP}.|seat|'auf' + place (wo? where?) → Dativ|s
Dat|Das Handy liegt in {NP}.|container|'in' + place (wo? where?) → Dativ|s
Dat|Ich fahre mit {NP} zur Arbeit.|veh|'mit' always takes the Dativ|s
Dat|Ich spreche mit {NP}.|person|'mit' always takes the Dativ|x
Dat|Er geht mit {NP} spazieren.|person walk|'mit' always takes the Dativ|x
Dat|Er spielt gern mit {NP}.|play|'mit' always takes the Dativ|x
Dat|Ich helfe {NP}.|person|'helfen' takes the Dativ (whom do I help?) → Dativ|x
Dat|Ich schenke {NP} ein Buch.|person|'schenken' + person = indirect object (to whom?) → Dativ|x
Dat|Ich gehe heute zu {NP}.|person|'zu' always takes the Dativ|x
Dat|Ich bekomme viel Hilfe von {NP}.|person|'von' always takes the Dativ|x
Dat|Ich komme gerade aus {NP}.|comefrom|'aus' always takes the Dativ|s
Dat|Nach {NP} gehe ich nach Hause.|event|'nach' always takes the Dativ|s
Dat|Ich esse das Brot mit {NP}.|topping|'mit' always takes the Dativ|x
Dat|Ich trinke den Kaffee mit {NP}.|addin|'mit' always takes the Dativ|x
Dat|Ich koche mit {NP}.|cook|'mit' always takes the Dativ|x
Gen|Wegen {NP} bleiben wir zu Hause.|wx|'wegen' takes the Genitiv|x
Gen|Trotz {NP} gehen wir spazieren.|wx|'trotz' takes the Genitiv|x
Gen|Wegen {NP} kommt er zu spät.|cause|'wegen' takes the Genitiv|x
Gen|Während {NP} schlafe ich schlecht.|time|'während' takes the Genitiv|x
Gen|Das Auto {NP} ist neu.|owner|Genitiv shows who something belongs to (whose car?) → Genitiv|
Gen|Das Haus {NP} ist schön.|owner|Genitiv shows who something belongs to (whose house?) → Genitiv|
""".replace("SMALL_LIKE", SMALL_LIKE)


# extra restrictions per frame template (tokens: N = no negative adjective, P = no price adjective,
# stems:a,b = allowed ein-words ("poss" = mein dein sein ihr unser), only:a,b = allowed adjectives)
NEG = {"schmutzig", "hässlich", "schlecht", "langweilig"}
PRICE = {"billig", "günstig"}
POSS = ["mein", "dein", "sein", "ihr", "unser"]
BAD_WEATHER = "only:kalt,stark,schlecht,groß,heiß,lang"
OVERRIDES = {
    "{NP} {gefällt/gefallen} mir sehr.": "N stems:ein,poss",
    "{NP} {schmeckt/schmecken} wirklich gut.": "N P",
    "{NP} {ist/sind} gesund.": "N P ban:gesund",
    "{NP} {ist/sind} heute im Angebot.": "N G M stems:ein,kein",
    "{NP} {hilft/helfen} uns oft.": "stems:poss",
    "{NP} {kommt/kommen} bald.": "stems:ein",
    "{NP} {bleibt/bleiben} zum Glück nicht lange.": "only:stark,kalt,heiß,schlecht,groß",
    "Ich kaufe {NP}.": "N ban:wichtig",
    "Ich brauche {NP}.": "N",
    "Ich suche {NP}.": "N ban:wichtig",
    "Heute trage ich {NP}.": "N ban:wichtig",
    "Zum Mittagessen esse ich {NP}.": "N P stems:ein,kein",
    "Zum Frühstück trinke ich {NP}.": "N P stems:ein,kein",
    "Im Café bestelle ich {NP}.": "N P stems:ein,kein",
    "Ich gehe nie ohne {NP} aus dem Haus.": "N stems:ein,poss",
    "Ich koche mit {NP}.": "P ban:heiß,kalt,warm",
    "Ich esse das Brot mit {NP}.": "P",
    "Ich trinke den Kaffee mit {NP}.": "P",
    "Wegen {NP} bleiben wir zu Hause.": BAD_WEATHER,
    "Trotz {NP} gehen wir spazieren.": BAD_WEATHER,
    "Wegen {NP} kommt er zu spät.": "stems:ein,poss",
    "Das Auto {NP} ist neu.": "stems:ein,poss",
    "Das Haus {NP} ist schön.": "stems:ein,poss",
    "Während {NP} schlafe ich schlecht.": "only:lang,kalt,heiß,warm,laut,anstrengend stems:ein",
}


def case_is_nom(c):
    return c == "Nom"


class Frame:
    def __init__(self, line):
        self.case, self.tpl, tags, self.why, mode = line.split("|")
        self.tags = set(tags.split())
        extra = OVERRIDES.get(self.tpl, "").split()
        self.sgonly = "s" in mode
        self.strong_ok = "x" in mode
        self.banned_adj = (NEG if "N" in extra else set()) | (PRICE if "P" in extra else set())
        self.mass_pl_only = "M" in extra
        if "G" in extra:
            self.banned_adj = self.banned_adj | {"gesund"}
        self.only_adj = None
        self.stems = None
        if case_is_nom(self.case) and not any(t.startswith("stems:") for t in extra):
            self.stems = {"ein", *POSS}
        for t in extra:
            if t.startswith("only:"):
                self.only_adj = set(t[5:].split(","))
            if t.startswith("ban:"):
                self.banned_adj = self.banned_adj | set(t[4:].split(","))
            if t.startswith("stems:"):
                self.stems = {x for st in t[6:].split(",") for x in (POSS if st == "poss" else [st])}
        assert self.tpl.count("{NP}") == 1, line


FRAME_LIST = [Frame(l) for l in FRAMES.strip().splitlines()]

# which declensions / cases belong to which difficulty level
LEVEL_OF = {}
for d in ("weak", "mixed"):
    for c in ("Nom", "Akk"):
        LEVEL_OF[(d, c)] = "A"
    LEVEL_OF[(d, "Dat")] = "B"
    LEVEL_OF[(d, "Gen")] = "C"
for c in ("Nom", "Akk", "Dat"):
    LEVEL_OF[("strong", c)] = "B"
LEVEL_OF[("strong", "Gen")] = "C"
PER_CELL = {"A": 14, "B": 14, "C": 10}
DECL_NAME = {"weak": "weak (after der / die / das, dieser)",
             "mixed": "mixed (after ein, kein, mein …)",
             "strong": "strong (no article)"}
DECL_SHORT = {"weak": "after der-word", "mixed": "after ein-word", "strong": "no article"}


def usable(noun, frame, decl, g):
    if not (noun.tags & frame.tags):
        return False
    if g == "pl":
        if noun.sgonly:
            return False
    else:
        if noun.g != g:
            return False
        if frame.sgonly is False and False:
            return False
        if decl == "strong" and not noun.sgonly:
            return False  # a countable singular noun is never used without an article
    if decl == "strong" and not frame.strong_ok:
        return False
    if frame.mass_pl_only and g != "pl" and not noun.sgonly:
        return False
    if decl == "mixed" and "wx" in noun.tags:
        return False  # "sein Regen", "meine Hitze" are not natural
    if g == "pl" and frame.sgonly:
        return False
    if frame.case == "Gen" and g != "pl" and noun.g in "mn" and not noun.gen:
        return False
    return bool(adjectives(noun, frame))


def adjectives(noun, frame):
    return [a for a in noun.adj if a not in frame.banned_adj and (frame.only_adj is None or a in frame.only_adj)]


def det_ok(noun, frame, decl, form, stem):
    if decl == "mixed":
        if frame.stems is not None and stem not in frame.stems:
            return False
        if noun.mass and stem == "ein":
            return False  # a substance does not take "ein"
        if any(stem == p for p in noun.noposs):
            return False
        if stem in POSS and noun.no_poss_at_all:
            return False
    return True


def plural_verb(tpl, g):
    return re.sub(r"\{([^{}/]+)/([^{}/]+)\}", lambda m: m.group(2) if g == "pl" else m.group(1), tpl)


def explain(noun, frame, decl, case, g, det, ending, np_done):
    gi = GENDERS.index(g)
    art = ARTICLE[g]
    if g == "pl":
        s1 = f"Noun: {noun.pl} → plural (all genders share one column)"
    else:
        extra = ", used without an article here (uncountable noun)" if decl == "strong" else ""
        s1 = f"Noun: {noun.sg} → {art} {noun.sg} ({GENDER_FULL[g]}, singular{extra})"
    s2 = f"Case: {frame.why}"
    if decl == "weak":
        s3 = (f"Determiner: '{det}' is a der-word → it already shows case and gender, "
              f"so the adjective only needs a 'light' ending")
        rule = "Rule (weak): -en everywhere, except -e in Nom m and in Nom/Akk f, n"
    elif decl == "mixed":
        if EIN_END[case][gi] == "":
            s3 = (f"Determiner: '{det}' (ein-word) has no ending in this slot → "
                  f"the adjective has to show gender and case itself")
        else:
            s3 = (f"Determiner: '{det}' (ein-word) already carries the ending -{EIN_END[case][gi]} → "
                  f"the adjective only needs a 'light' ending")
        rule = "Rule (mixed): like weak, but where 'ein' has no ending (Nom m, Nom/Akk n) → -er / -es"
    else:
        dw = DEF[case][gi]
        s3 = f"No determiner → the adjective must show case and gender itself, like the missing '{dw}'"
        rule = "Rule (strong): the adjective takes the der-word ending (exception: Gen m, n → -en)"
    s4 = f"{rule}\n   {decl} · {CASE_FULL[case]} · {g} → -{ending}"
    steps = [s1, s2, s3, s4]
    return "\n".join([f"{i}. {s}" for i, s in enumerate(steps, 1)] + [f"∴ -{ending}  →  {np_done}"])


def build():
    out = []
    for decl in ("weak", "mixed", "strong"):
        for case in CASES:
            for g in GENDERS:
                level = LEVEL_OF[(decl, case)]
                quota = PER_CELL[level]
                ending = ENDINGS[decl][case][GENDERS.index(g)]
                rng = random.Random(zlib.crc32(f"{decl}{case}{g}".encode()))
                frames = [f for f in FRAME_LIST if f.case == case]
                pairs = [(f, n) for f in frames for n in NOUN_LIST if usable(n, f, decl, g)]
                nouns = {n.sg for _, n in pairs}
                assert pairs, (decl, case, g)
                cap = max(2, math.ceil(quota / len(nouns)))
                fcap = max(2, math.ceil(quota / len({f.tpl for f, _ in pairs})))
                rng.shuffle(pairs)
                used_n, used_f, seen, made = Counter(), Counter(), set(), 0
                # several passes: first strict caps, then relaxed
                for relax in (0, 1, 2, 3):
                    for f, n in pairs:
                        if made >= quota:
                            break
                        if used_n[n.sg] >= cap + relax or used_f[f.tpl] >= fcap + relax:
                            continue
                        dets = [d for d in determiners(decl, case, g) if det_ok(n, f, decl, d[0], d[1])]
                        if not dets:
                            continue
                        det = rng.choice(dets)[0]
                        adj = rng.choice(adjectives(n, f))
                        np_ = " ".join(x for x in [det, adj + "___", n.form(case, g)] if x)
                        sentence = plural_verb(f.tpl, g).replace("{NP}", np_)
                        sentence = sentence[0].upper() + sentence[1:]
                        if sentence in seen:
                            continue
                        seen.add(sentence)
                        used_n[n.sg] += 1
                        used_f[f.tpl] += 1
                        made += 1
                        assert sentence.count("___") == 1, sentence
                        out.append({
                            "id": "", "level": level, "type": "adjective_ending", "sentence": sentence,
                            "options": OPTIONS, "answer": ending, "case": CASE_FULL[case],
                            "focus": f"{DECL_SHORT[decl]} · {case} · {g}",
                            "explanation": explain(n, f, decl, case, g, det, ending, np_.replace("___", ending)),
                            "tags": ["adjective-ending", decl, CASE_FULL[case].lower(), g],
                            "ref": {"table": "adjective", "row": f"{decl} {case}", "col": g},
                        })
                    if made >= quota:
                        break
    return out


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "data")
    ex = build()
    rng = random.Random(11)
    ex.sort(key=lambda x: x["level"])
    for lv in "ABC":
        idx = [i for i, x in enumerate(ex) if x["level"] == lv]
        part = [ex[i] for i in idx]
        rng.shuffle(part)
        for i, p in zip(idx, part):
            ex[i] = p
    for i, x in enumerate(ex, 1):
        x["id"] = f"J-{i:04d}"
    with open(os.path.join(out_dir, "adj.json"), "w", encoding="utf-8") as fh:
        json.dump(ex, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    cells = Counter((x["tags"][1], x["tags"][2], x["tags"][3]) for x in ex)
    print(f"{len(ex)} exercises  levels {dict(Counter(x['level'] for x in ex))}  answers {dict(Counter(x['answer'] for x in ex))}")
    print("smallest cells:", sorted(cells.items(), key=lambda kv: kv[1])[:6])


if __name__ == "__main__":
    main()
