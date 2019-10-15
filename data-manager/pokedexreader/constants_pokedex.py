"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2019  Mirek Długosz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""


XY_MEGAS = ["venusaurmega", "charizardmegax", "charizardmegay",
            "blastoisemega", "alakazammega", "gengarmega", "kangaskhanmega",
            "pinsirmega", "gyaradosmega", "aerodactylmega", "mewtwomegax",
            "mewtwomegay", "ampharosmega", "scizormega", "heracrossmega",
            "houndoommega", "tyranitarmega", "blazikenmega", "gardevoirmega",
            "mawilemega", "aggronmega", "medichammega", "manectricmega",
            "banettemega", "absolmega", "garchompmega", "lucariomega",
            "abomasnowmega"]

ORAS_MEGAS = XY_MEGAS + ["beedrillmega", "pidgeotmega", "slowbromega",
    "steelixmega", "sceptilemega", "swampertmega", "sableyemega",
    "sharpedomega", "cameruptmega", "altariamega", "glaliemega",
    "salamencemega", "metagrossmega", "latiasmega", "latiosmega",
    "rayquazamega", "lopunnymega", "gallademega", "audinomega", "dianciemega",
    "crucibellemega"]

# List of Pokemon available in each game. This is required, since Game Freak
# broke the assumption that all Pokemon available in previous game/generation
# are available in new game/generation as well
# It's part of constants, but sheer size caused it to be moved to separate file
GEN1_DEX = ["bulbasaur", "ivysaur", "venusaur", "charmander",
            "charmeleon", "charizard", "squirtle", "wartortle",
            "blastoise", "caterpie", "metapod", "butterfree", "weedle",
            "kakuna", "beedrill", "pidgey", "pidgeotto", "pidgeot",
            "rattata", "raticate", "spearow", "fearow", "ekans", "arbok",
            "pikachu", "raichu", "sandshrew", "sandslash", "nidoranf",
            "nidorina", "nidoqueen", "nidoranm", "nidorino", "nidoking",
            "clefairy", "clefable", "vulpix", "ninetales", "jigglypuff",
            "wigglytuff", "zubat", "golbat", "oddish", "gloom",
            "vileplume", "paras", "parasect", "venonat", "venomoth",
            "diglett", "dugtrio", "meowth", "persian", "psyduck",
            "golduck", "mankey", "primeape", "growlithe", "arcanine",
            "poliwag", "poliwhirl", "poliwrath", "abra", "kadabra",
            "alakazam", "machop", "machoke", "machamp", "bellsprout",
            "weepinbell", "victreebel", "tentacool", "tentacruel",
            "geodude", "graveler", "golem", "ponyta", "rapidash",
            "slowpoke", "slowbro", "magnemite", "magneton", "farfetchd",
            "doduo", "dodrio", "seel", "dewgong", "grimer", "muk",
            "shellder", "cloyster", "gastly", "haunter", "gengar", "onix",
            "drowzee", "hypno", "krabby", "kingler", "voltorb",
            "electrode", "exeggcute", "exeggutor", "cubone", "marowak",
            "hitmonlee", "hitmonchan", "lickitung", "koffing", "weezing",
            "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan",
            "horsea", "seadra", "goldeen", "seaking", "staryu", "starmie",
            "mrmime", "scyther", "jynx", "electabuzz", "magmar", "pinsir",
            "tauros", "magikarp", "gyarados", "lapras", "ditto", "eevee",
            "vaporeon", "jolteon", "flareon", "porygon", "omanyte",
            "omastar", "kabuto", "kabutops", "aerodactyl", "snorlax",
            "articuno", "zapdos", "moltres", "dratini", "dragonair",
            "dragonite", "mewtwo", "mew"]
GEN2_DEX = GEN1_DEX + ["chikorita", "bayleef", "meganium", "cyndaquil", "quilava",
            "typhlosion", "totodile", "croconaw", "feraligatr",
            "sentret", "furret", "hoothoot", "noctowl", "ledyba",
            "ledian", "spinarak", "ariados", "crobat", "chinchou",
            "lanturn", "pichu", "cleffa",
            "igglybuff", "togepi", "togetic", "natu", "xatu", "mareep",
            "flaaffy", "ampharos", "bellossom", "marill", "azumarill",
            "sudowoodo", "politoed", "hoppip", "skiploom", "jumpluff",
            "aipom", "sunkern", "sunflora", "yanma", "wooper",
            "quagsire", "espeon", "umbreon", "murkrow", "slowking",
            "misdreavus", "unown", "wobbuffet", "girafarig", "pineco",
            "forretress", "dunsparce", "gligar", "steelix", "snubbull",
            "granbull", "qwilfish", "scizor", "shuckle", "heracross",
            "sneasel", "teddiursa", "ursaring", "slugma", "magcargo",
            "swinub", "piloswine", "corsola", "remoraid", "octillery",
            "delibird", "mantine", "skarmory", "houndour", "houndoom",
            "kingdra", "phanpy", "donphan", "porygon2", "stantler",
            "smeargle", "tyrogue", "hitmontop", "smoochum", "elekid",
            "magby", "miltank", "blissey", "raikou", "entei",
            "suicune", "larvitar", "pupitar", "tyranitar", "lugia",
            "hooh", "celebi"]
GEN3_DEX = GEN2_DEX + ["treecko", "grovyle", "sceptile", "torchic", "combusken",
            "blaziken", "mudkip", "marshtomp", "swampert",
            "poochyena", "mightyena", "zigzagoon", "linoone",
            "wurmple", "silcoon", "beautifly", "cascoon", "dustox",
            "lotad", "lombre", "ludicolo", "seedot", "nuzleaf",
            "shiftry", "taillow", "swellow", "wingull", "pelipper",
            "ralts", "kirlia", "gardevoir", "surskit", "masquerain",
            "shroomish", "breloom", "slakoth", "vigoroth", "slaking",
            "nincada", "ninjask", "shedinja", "whismur", "loudred",
            "exploud", "makuhita", "hariyama", "azurill", "nosepass",
            "skitty", "delcatty", "sableye", "mawile", "aron",
            "lairon", "aggron", "meditite", "medicham", "electrike",
            "manectric", "plusle", "minun", "volbeat", "illumise",
            "roselia", "gulpin", "swalot", "carvanha", "sharpedo",
            "wailmer", "wailord", "numel", "camerupt", "torkoal",
            "spoink", "grumpig", "spinda", "trapinch", "vibrava",
            "flygon", "cacnea", "cacturne", "swablu", "altaria",
            "zangoose", "seviper", "lunatone", "solrock", "barboach",
            "whiscash", "corphish", "crawdaunt", "baltoy", "claydol",
            "lileep", "cradily", "anorith", "armaldo", "feebas",
            "milotic", "castform", "kecleon", "shuppet", "banette",
            "duskull", "dusclops", "tropius", "chimecho", "absol",
            "wynaut", "snorunt", "glalie", "spheal", "sealeo",
            "walrein", "clamperl", "huntail", "gorebyss",
            "relicanth", "luvdisc", "bagon", "shelgon", "salamence",
            "beldum", "metang", "metagross", "regirock", "regice",
            "registeel", "latias", "latios", "kyogre", "groudon",
            "rayquaza", "jirachi", ]
GEN4_DEX = GEN3_DEX + ["deoxys", "deoxysattack", "deoxysdefense",
            "deoxysspeed"] + ["turtwig", "grotle", "torterra", "chimchar",
            "monferno", "infernape", "piplup", "prinplup", "empoleon",
            "starly", "staravia", "staraptor", "bidoof", "bibarel",
            "kricketot", "kricketune", "shinx", "luxio", "luxray",
            "budew", "roserade", "cranidos", "rampardos", "shieldon",
            "bastiodon", "burmy", "wormadam", "wormadamsandy",
            "wormadamtrash", "mothim", "combee", "vespiquen",
            "pachirisu", "buizel", "floatzel", "cherubi", "cherrim",
            "shellos", "gastrodon", "ambipom",
            "drifloon", "drifblim", "buneary", "lopunny",
            "mismagius", "honchkrow", "glameow", "purugly",
            "chingling", "stunky", "skuntank", "bronzor", "bronzong",
            "bonsly", "mimejr", "happiny", "chatot", "spiritomb",
            "gible", "gabite", "garchomp", "munchlax", "riolu",
            "lucario", "hippopotas", "hippowdon", "skorupi",
            "drapion", "croagunk", "toxicroak", "carnivine",
            "finneon", "lumineon", "mantyke", "snover", "abomasnow",
            "weavile", "magnezone", "lickilicky", "rhyperior",
            "tangrowth", "electivire", "magmortar", "togekiss",
            "yanmega", "leafeon", "glaceon", "gliscor", "mamoswine",
            "porygonz", "gallade", "probopass", "dusknoir",
            "froslass", "rotom", "rotomheat", "rotomwash",
            "rotomfrost", "rotomfan", "rotommow", "uxie", "mesprit",
            "azelf", "dialga", "palkia", "heatran", "regigigas",
            "giratina", "giratinaorigin", "cresselia", "phione",
            "manaphy", "darkrai", "shaymin", "shayminsky", "arceus",
            "arceusbug", "arceusdark", "arceusdragon",
            "arceuselectric", "arceusfairy", "arceusfighting",
            "arceusfire", "arceusflying", "arceusghost",
            "arceusgrass", "arceusground", "arceusice",
            "arceuspoison", "arceuspsychic", "arceusrock",
            "arceussteel", "arceuswater"]
GEN5_DEX = GEN4_DEX + ["victini", "snivy", "servine", "serperior", "tepig",
            "pignite", "emboar", "oshawott", "dewott", "samurott",
            "patrat", "watchog", "lillipup", "herdier", "stoutland",
            "purrloin", "liepard", "pansage", "simisage", "pansear",
            "simisear", "panpour", "simipour", "munna", "musharna",
            "pidove", "tranquill", "unfezant", "blitzle", "zebstrika",
            "roggenrola", "boldore", "gigalith", "woobat", "swoobat",
            "drilbur", "excadrill", "audino", "timburr", "gurdurr",
            "conkeldurr", "tympole", "palpitoad", "seismitoad",
            "throh", "sawk", "sewaddle", "swadloon", "leavanny",
            "venipede", "whirlipede", "scolipede", "cottonee",
            "whimsicott", "petilil", "lilligant", "basculin",
            "basculinbluestriped", "sandile", "krokorok", "krookodile",
            "darumaka", "darmanitan", "darmanitanzen", "maractus",
            "dwebble", "crustle", "scraggy", "scrafty", "sigilyph",
            "yamask", "cofagrigus", "tirtouga", "carracosta", "archen",
            "archeops", "trubbish", "garbodor", "zorua", "zoroark",
            "minccino", "cinccino", "gothita", "gothorita",
            "gothitelle", "solosis", "duosion", "reuniclus",
            "ducklett", "swanna", "vanillite", "vanillish",
            "vanilluxe", "deerling", "sawsbuck", "emolga",
            "karrablast", "escavalier", "foongus", "amoonguss",
            "frillish", "jellicent", "alomomola", "joltik",
            "galvantula", "ferroseed", "ferrothorn", "klink", "klang",
            "klinklang", "tynamo", "eelektrik", "eelektross", "elgyem",
            "beheeyem", "litwick", "lampent", "chandelure", "axew",
            "fraxure", "haxorus", "cubchoo", "beartic", "cryogonal",
            "shelmet", "accelgor", "stunfisk", "mienfoo", "mienshao",
            "druddigon", "golett", "golurk", "pawniard", "bisharp",
            "bouffalant", "rufflet", "braviary", "vullaby",
            "mandibuzz", "heatmor", "durant", "deino", "zweilous",
            "hydreigon", "larvesta", "volcarona", "cobalion",
            "terrakion", "virizion", "tornadus",
            "thundurus", "reshiram", "zekrom",
            "landorus", "kyurem", "kyuremblack",
            "kyuremwhite", "keldeo", "meloetta",
            "genesect", "genesectdouse",
            "genesectshock", "genesectburn", "genesectchill"]
GEN6_DEX = GEN5_DEX + ["chespin", "quilladin", "chesnaught", "fennekin", "braixen",
            "delphox", "froakie", "frogadier", "greninja", "greninjaash",
            "bunnelby", "diggersby", "fletchling", "fletchinder", "talonflame",
            "scatterbug", "spewpa", "vivillon", "litleo", "pyroar", "flabebe", "floette",
            "florges", "skiddo", "gogoat", "pancham",
            "pangoro", "furfrou", "espurr", "meowstic", "meowsticf", "honedge",
            "doublade", "aegislash", "spritzee",
            "aromatisse", "swirlix", "slurpuff", "inkay", "malamar", "binacle",
            "barbaracle", "skrelp", "dragalge", "clauncher", "clawitzer",
            "helioptile", "heliolisk", "tyrunt", "tyrantrum", "amaura",
            "aurorus", "sylveon", "hawlucha", "dedenne", "carbink", "goomy",
            "sliggoo", "goodra", "klefki", "phantump", "trevenant",
            "pumpkaboo", "pumpkaboosmall", "pumpkaboolarge", "pumpkaboosuper",
            "gourgeist", "gourgeistsmall", "gourgeistlarge", "gourgeistsuper",
            "bergmite", "avalugg", "noibat", "noivern", "xerneas", "yveltal",
            "zygarde", "diancie",
            "hoopa", "hoopaunbound", "volcanion"]
GEN7_DEX = GEN6_DEX + ORAS_MEGAS + ["zygarde10", "zygardecomplete"] + ["rowlet",
            "dartrix", "decidueye", "litten",
            "torracat", "incineroar", "popplio", "brionne", "primarina",
            "pikipek", "trumbeak", "toucannon", "yungoos", "gumshoos",
            "grubbin", "charjabug", "vikavolt", "crabrawler", "crabominable",
            "oricorio", "oricoriopompom", "oricoriopau", "oricoriosensu",
            "cutiefly", "ribombee", "rockruff", "lycanroc", "lycanrocmidnight",
            "lycanrocdusk", "wishiwashi", "mareanie",
            "toxapex", "mudbray", "mudsdale", "dewpider", "araquanid",
            "fomantis", "lurantis", "morelull", "shiinotic", "salandit",
            "salazzle", "stufful", "bewear", "bounsweet", "steenee",
            "tsareena", "comfey", "oranguru", "passimian", "wimpod",
            "golisopod", "sandygast", "palossand", "pyukumuku",
            "typenull", "silvally", "silvallybug", "silvallydark",
            "silvallydragon", "silvallyelectric", "silvallyfairy",
            "silvallyfighting", "silvallyfire", "silvallyflying",
            "silvallyghost", "silvallygrass", "silvallyground",
            "silvallyice", "silvallypoison", "silvallypsychic",
            "silvallyrock", "silvallysteel", "silvallywater", "minior",
            "komala", "turtonator", "togedemaru", "mimikyu",
            "bruxish", "drampa", "dhelmise", "jangmoo",
            "hakamoo", "kommoo", "tapukoko", "tapulele", "tapubulu",
            "tapufini", "cosmog", "cosmoem", "solgaleo", "lunala", "nihilego",
            "buzzwole", "pheromosa", "xurkitree", "celesteela", "kartana",
            "guzzlord", "necrozma", "magearna", "marshadow"]

available_pokemon = {
    "red-blue": GEN1_DEX,
    "yellow": GEN1_DEX,
    "gold-silver": GEN2_DEX,
    "crystal": GEN2_DEX,
    "ruby-sapphire": GEN3_DEX + ["deoxys"],
    "emerald": GEN3_DEX + ["deoxysspeed"],
    "firered-leafgreen": GEN3_DEX + ["deoxysattack", "deoxysdefense"],
    "diamond-pearl": GEN4_DEX,
    "platinum": GEN4_DEX,
    "heartgold-soulsilver": GEN4_DEX,
    "black-white": GEN5_DEX,
    "black-2-white-2": GEN5_DEX,
    "x-y": GEN6_DEX + XY_MEGAS,
    "omega-ruby-alpha-sapphire": GEN6_DEX + ORAS_MEGAS,
    "sun-moon": GEN7_DEX,
    "ultra-sun-ultra-moon": GEN7_DEX + ["necrozmaduskmane", "necrozmadawnwings",
            "necrozmaultra", "poipole", "naganadel", "stakataka", "blacephalon",
            "zeraora"]
}
