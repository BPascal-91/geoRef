#!/usr/bin/env python3

import bpaTools

### Constantes ###
oFranceNames = {"0":"France-Metropolitaine",
                "1":"Guyane-Francaise",
                "2":"Corse",
                "3":"LaReunion",
                "4":"Antilles-Martinique",
                "5":"Antilles-Guadeloupe-BasseTerre",
                "6":"Antilles-Guadeloupe-GrandeTerre",
                "7":"Mayotte-GrandeTerre",
                "8":"France-IleDOleron",
                "9":"Antilles-MarieGalante",
                "10":"France-BelleIle",
                "11":"France-IleDeRe",
                "12":"France-IleNoirmoutier",
                "13":"Antilles-IleSaintMartin-Francaise",
                "14":"France-IleDYeu",
                "15":"France-IleOuessant",
                "16":"France-PresquIleQuiberon",
                "17":"France-IleGroix",
                "18":"Antilles-LaDesirade",
                "19":"France-IlePorquerolles",
                "20":"France-IleDuLevant",
                "21":"Mayotte-PetiteTerre",
                "22":"France-IlePortCros",
                "23":"Antilles-IleDesSaintes-TerreDeBas",
                "24":"France-IleDePatiras",
                "25":"France-IleDHouat",
                "26":"France-IleDeBatz",
                "27":"Antilles-IleSaintMartin-TerresBasses",
                "28":"France-IleAuxMoines",
                "29":"Antilles-IleDesSaintes-TerreDeHaut",
                "30":"France-IleDeBrehat",
                "31":"Guyane-Francaise-Awala",
                "32":"France-IleDeHoedic",
                "33":"France-Dunkerque-Terminal",
                "34":"France-IlesDuFrioul",
                "35":"France-IleDArz",
                "36":"Mayotte-Mtsambro",
                "37":"France-IleNouvelle",
                "38":"France-IleSainteMarguerite",
                "39":"France-IleGrande",
                "40":"France-IleDAix",
                "41":"France-PresquIleGraves-Est",
                "42":"France-PortSaintLouisDuRhone-PlageNapoleonNord",
                "43":"Antilles-IleDeLaPetiteTerre",
                "44":"Corse-IleCavallo",
                "45":"France-IleDeMalprat",
                "46":"Antilles-IletAFayou",
                "47":"France-PresquIlePenerf",
                "48":"France-IleDesEmbiez",
                "49":"France-IleMolene",
                "50":"France-IleRiou",
                "51":"Antilles-IleTintamarre",
                "52":"France-VasardDeBeychevelle",
                "53":"France-LavauSurLoire1",
                "54":"France-IleMadame",
                "55":"France-PresquIleGraves-Ouest",
                "56":"France-IleDeBreniguet",
                "57":"France-BancDArguin1",
                "58":"France-IleTascon",
                "59":"Antilles-GrandIlet",
                "60":"Mayotte-IlotMbouzi",
                "61":"Corse-IleLavezzu",
                "62":"France-IleDeBagaud",
                "63":"France-IleIlur",
                "64":"France-PresquIleLePlec",
                "65":"France-ArcachonIlot1",
                "66":"France-GrandeIle",
                "67":"Antilles-Martinique-IletChancel",
                "68":"Antilles-IleSaintMartin-Marigot1",
                "69":"France-IleDuLoch",
                "70":"France-IleSaintHonorat",
                "71":"France-IleDeBrehat-Est",
                "72":"Guyane-Francaise-IletDeRemire",
                "73":"Corse-ArchipelDesSanguinaires",
                "74":"France-IleTatihou",
                "75":"Antilles-Martinique-IletsOscarThierry",
                "76":"France-IleKeller",
                "77":"France-IleDArz-Est",
                "78":"France-IleEr",
                "79":"France-PresquIleKermorvan",
                "80":"France-IlePenfret",
                "81":"France-IleCallot-Nord",
                "82":"France-IleMaire",
                "83":"France-IleLongue",
                "84":"Antilles-IleDesSaintes-IletACabrit",
                "85":"France-PresquIleLaVilleneuve",
                "86":"France-IleMilliau",
                "87":"Guyane-Francaise-IlesRemire",
                "88":"France-IleDeBoed-Ouest",
                "89":"France-IleSansNom",
                "90":"France-PrequIleMontsarrac",
                "91":"France-PrequIleSaintLaurent",
                "92":"France-IleDeBoedic",
                "93":"France-IleDeSiek",
                "94":"France-IlesDesMortsTreberon",
                "95":"Guyane-Francaise-IleRoyale",
                "96":"France-IleDeSein-Est",
                "97":"France-IleBeniguet",
                "98":"France-IleMaudez",
                "99":"France-IleAganton",
                "100":"France-IleCallot-Centre",
                "101":"France-IleSaintGildas",
                "102":"France-IleTome",
                "103":"France-IleDeSein-Ouest",
                "104":"France-IleABois",
                "105":"France-IleBono",
                "106":"France-IleGarvinis",
                "107":"Antilles-Guadeloupe-IletACochons",
                "108":"France-IleDesEbihens",
                "109":"France-IleQuemenes-Est",
                "110":"Corse-IlePinarellu",
                "111":"Guyane-Francaise-IletLesMamellesOuest",
                "112":"Guyane-Francaise-IleSaintJoseph",
                "113":"Guyane-Francaise-IleDuDiableNord",
                "114":"Mayotte-PrequilHandrema-Nord",
                "115":"Mayotte-IlotHandrema-Ouest",
                "116":"Mayotte-PointeBandraboua",
                "117":"Mayotte-IlotPamandziKeli",
                "118":"Mayotte-PresquilDzagudzi-Ouest",
                "119":"Mayotte-IlotBrandrele",
                "120":"Mayotte-IlotKaroni",
                "121":"Mayotte-IlotDeSableBlanc",
                "122":"Antilles-Martinique-IletAChevalier",
                "123":"Antilles-Martinique-RocherDuDiamand",
                "124":"Antilles-Martinique-GrosIlet",
                "125":"Antilles-Martinique-IleDeLaPetiteGrenade",
                "126":"Antilles-Martinique-IletLong",
                "127":"Antilles-Martinique-IleMetrente",
                "128":"Antilles-Martinique-IletLavigne",
                "129":"Corse-IleCerbicale",
                "130":"Antilles-Guadeloupe-IletsPigeon",
                "131":"Antilles-Guadeloupe-IletAKahouanne",
                "132":"Antilles-IleSaintMartin-PointeDuBluff",
                "133":"Antilles-IleSaintMartin-IletDePinel",
                "134":"Corse-IleDeLaPietra",
                "135":"France-PresquIlePenerf-Liaison",
                "136":"France-IleCalseraigne",
                "137":"France-IlePate",
                "138":"France-IleVenan",
                "139":"France-IleDeLaJument",
                "140":"France-PrequIleDeLaHougue",
                "141":"France-Marseille-TerminalQuaiDesCroisieres",
                "142":"France-Toulon-QuaiDuPortMilitaire",
                "143":"France-Dunkerque-DigueDuBraek",
                "144":"France-IleDeBoed-Est",
                "145":"France-IleLeGrandRibaud",
                "146":"France-IleDeTrielen",
                "147":"France-IleEnezTerch",
                "148":"France-IleDeJarre-Centre",
                "149":"Corse-IleDePiana",
                "150":"Corse-IleDePietricaggiosa",
                "151":"Corse-IleDeForana",
                "152":"France-IleVerte",
                "153":"Corse-PrequIleParata",
                "154":"France-IleDuGrandGaou",
                "155":"France-PrequIleDuLangoustier",
                "156":"Corse-IleCapense",
                "157":"Corse-IleDeLaGiraglia",
                "158":"France-IleDuGrandRenouveau",
                "159":"France-IleDeBendor",
                "160":"France-CapTaillat",
                "161":"France-PointeDeLaCacau",
                "162":"France-IleDYoch",
                "163":"France-BancDArguin2",
                "164":"France-IleDeBalanec",
                "165":"France-IleDeTrompeLoup",
                "166":"France-IleIrus",
                "167":"France-PresquIleLaCayenne",
                "168":"France-PointeDeLaFumee1",
                "169":"France-PointeDeLaFumee2",
                "170":"France-LaRochelle-QuaiConstantBrisson",
                "171":"France-LaRochelle-MoleDEscale",
                "172":"France-LaFauteSurMer-PlageLaGrandeCasse1",
                "173":"France-LaFauteSurMer-PlageLaGrandeCasse2",
                "174":"France-IleAuxChevaux",
                "175":"France-IleSaintNicolasDesGlenan",
                "176":"France-IleValueg",
                "177":"France-IleDumet",
                "178":"France-PointeDePenvis",
                "179":"France-PrequIleDeTruscat",
                "180":"France-PointeDuBrehuidic",
                "181":"France-PointeDeSaintNicolas",
                "182":"France-IleStibiden",
                "183":"France-PointeErlong",
                "184":"France-IleBrannec",
                "185":"France-IleGodec",
                "186":"France-IleIluric",
                "187":"France-PointeDeMenErBellec",
                "188":"France-IleDeBailleron",
                "189":"France-IleErRunio",
                "190":"France-SeptIles",
                "191":"France-PointeDeBerno",
                "192":"France-IleAuxMoines-PointeDeToulindac",
                "193":"France-IleDArz-PointeDuBelure",
                "194":"France-IleDeConleau",
                "195":"France-IleDeRiech",
                "196":"France-IleDeNiheu",
                "197":"France-IleKerner",
                "198":"France-CornNeguan",
                "199":"France-IleDeDrenec",
                "200":"France-IleAuxMoutons",
                "201":"France-IleRaguenez",
                "202":"France-IleKelaourou",
                "203":"France-IleTristan",
                "204":"France-IleDeLAber",
                "205":"France-IleDeTerenez",
                "206":"France-IleQuemenes-Ouest",
                "207":"France-IleDeLedenezQuemenes",
                "208":"France-IleDeLedenezVraz",
                "209":"France-IleRenote",
                "210":"France-IleDeBannec-Sud",
                "211":"France-PrequIleDuVivier",
                "212":"France-IleGuennioc",
                "213":"France-PennEnez",
                "214":"France-MontSaintMichel",
                "215":"France-IleVierge",
                "216":"France-PointeKeremma",
                "217":"France-IleCallot-Sud",
                "218":"France-MezDeGoelo",
                "219":"France-IleLosquet",
                "220":"France-IleSaintRiom",
                "221":"France-IleAval",
                "222":"France-IleRaguenes",
                "223":"France-IleLogodec",
                "224":"France-IleDuMilieu",
                "225":"France-IleBalanec",
                "226":"France-IleLoaven",
                "227":"France-LaPetiteIle",
                "228":"France-IleAuxMoinesSeptIles",
                "229":"France-IleRouzic",
                "230":"France-PointeDesSalines",
                "231":"France-IleDeSein-Centre",
                "232":"France-PresquIleQuiberon-PointeDuConguel",
                "233":"France-PresquIleQuiberon-PlageDuConguel",
                "234":"France-PresquIlePenerf-PointeDuBile",
                "235":"France-IleGovihan-Nord",
                "236":"France-IleGovihan-Sud",
                "237":"France-IleDeBannec-Nord"
                }

aFrance = ["France-Metropolitaine",
           "France-IleDOleron",
           "France-BelleIle",
           "France-IleDRe",
           "France-IleNoirmoutier",
           "France-IleDYeu",
           "France-IleOuessant",
           "France-PresquIleQuiberon",
           "France-PresquIleQuiberon-PointeDuConguel",
           "France-PresquIleQuiberon-PlageDuConguel",
           "France-IleGroix",
           "France-IlePorquerolles",
           "France-IleDuLevant",
           "France-IlePortCros",
           "France-IleDePatiras",
           "France-IleDHouat",
           "France-IleDeBatz",
           "France-IleAuxMoines",
           "France-IleAuxMoines-PointeDeToulindac",
           "France-IleDeBrehat",
           "France-IleDeHoedic",
           "France-Dunkerque-Terminal",
           "France-Dunkerque-DigueDuBraek",
           "France-IlesDuFrioul",
           "France-IleDArz",
           "France-IleDArz-Est",
           "France-IleDArz-PointeDuBelure",
           "France-IleNouvelle",
           "France-IleSainteMarguerite",
           "France-IleGrande",
           "France-IleDAix",
           "France-PresquIleGraves-Est",
           "France-PresquIleGraves-Ouest",
           "France-PortSaintLouisDuRhone-PlageNapoleon-Nord",
           "France-IleDeMalprat",
           "France-PresquIlePenerf",
           "France-PresquIlePenerf-Liaison",
           "France-PresquIlePenerf-PointeDuBile",
           "France-IleDesEmbiez",
           "France-IleMolene",
           "France-IleRiou",
           "France-VasardDeBeychevelle",
           "France-IlePate",
           "France-LavauSurLoire1",
           "France-IleMadame",
           "France-IleDeBreniguet",
           "France-BancDArguin1",
           "France-BancDArguin2",
           "France-IleTascon",
           "France-IleDeBagaud",
           "France-IleIlur",
           "France-PresquIleLePlec",
           "France-ArcachonIlot1",
           "France-GrandeIle",
           "France-IleDuLoch",
           "France-IleSaintHonorat",
           "France-IleDeBrehat-Est",
           "France-IleTatihou",
           "France-IleEr",
           "France-PresquIleKermorvan",
           "France-IlePenfret",
           "France-IleCallot-Nord",
           "France-IleCallot-Centre",
           "France-IleCallot-Sud",
           "France-IleMaire",
           "France-IleLongue",
           "France-PresquIleLaVilleneuve",
           "France-IleMilliau",
           "France-IleSansNom",
           "France-PrequIleMontsarrac",
           "France-PrequIleSaintLaurent",
           "France-IleDeBoedic",
           "France-IleDeBoed-Ouest",
           "France-IleDeBoed-Est",
           "France-IleDeSiek",
           "France-IlesDesMortsTreberon",
           "France-IleDeSein-Est",
           "France-IleDeSein-Centre",
           "France-IleDeSein-Ouest",
           "France-IleBeniguet",
           "France-IleMaudez",
           "France-IleAganton",
           "France-IleSaintGildas",
           "France-IleTome",
           "France-IleABois",
           "France-IleBono",
           "France-IleGarvinis",
           "France-IleDesEbihens",
           "France-IleQuemenes-Est",
           "France-IleQuemenes-Ouest",
           "France-IleDeLedenezQuemenes",
           "France-IleCalseraigne",
           "France-IleVenan",
           "France-IleDeLaJument",
           "France-PrequIleDeLaHougue",
           "France-Marseille-TerminalQuaiDesCroisieres",
           "France-Toulon-QuaiDuPortMilitaire",
           "France-Dunkerque-DigueDuBraek",
           "France-IleLeGrandRibaud",
           "France-IleDeTrielen",
           "France-IleEnezTerch",
           "France-IleDeJarre-Centre",
           "France-IleVerte",
           "France-IleDuGrandGaou",
           "France-PrequIleDuLangoustier",
           "France-IleDuGrandRenouveau",
           "France-IleDeBendor",
           "France-CapTaillat",
           "France-PointeDeLaCacau",
           "France-IleDYoch",
           "France-IleDeBalanec",
           "France-IleDeTrompeLoup",
           "France-IleIrus",
           "France-PresquIleLaCayenne",
           "France-PointeDeLaFumee1",
           "France-PointeDeLaFumee2",
           "France-LaRochelle-QuaiConstantBrisson",
           "France-LaRochelle-MoleDEscale",
           "France-LaFauteSurMer-PlageLaGrandeCasse1",
           "France-LaFauteSurMer-PlageLaGrandeCasse2",
           "France-IleAuxChevaux",
           "France-IleSaintNicolasDesGlenan",
           "France-IleValueg",
           "France-IleDumet",
           "France-PointeDePenvis",
           "France-PrequIleDeTruscat",
           "France-PointeDuBrehuidic",
           "France-PointeDeSaintNicolas",
           "France-IleStibiden",
           "France-PointeErlong",
           "France-IleBrannec",
           "France-IleGodec",
           "France-IleIluric",
           "France-PointeDeMenErBellec",
           "France-IleDeBailleron",
           "France-IleErRunio",
           "France-SeptIles",
           "France-PointeDeBerno",
           "France-IleDeConleau",
           "France-IleDeRiech",
           "France-IleDeNiheu",
           "France-IleKerner",
           "France-CornNeguan",
           "France-IleDeDrenec",
           "France-IleAuxMoutons",
           "France-IleRaguenez",
           "France-IleKelaourou",
           "France-IleTristan",
           "France-IleDeLAber",
           "France-IleDeTerenez",
           "France-IleDeLedenezVraz",
           "France-IleRenote",
           "France-PrequIleDuVivier",
           "France-IleGuennioc",
           "France-PennEnez",
           "France-MontSaintMichel",
           "France-IleVierge",
           "France-PointeKeremma",
           "France-MezDeGoelo",
           "France-IleLosquet",
           "France-IleSaintRiom",
           "France-IleAval",
           "France-IleRaguenes",
           "France-IleLogodec",
           "France-IleDuMilieu",
           "France-IleBalanec",
           "France-IleLoaven",
           "France-LaPetiteIle",
           "France-IleAuxMoinesSeptIles",
           "France-IleRouzic",
           "France-PointeDesSalines",
           "France-IleGovihan-Nord",
           "France-IleGovihan-Sud",
           "France-IleDeBannec-Sud",
           "France-IleDeBannec-Nord"
           ]

aCorse = ["Corse",
          "Corse-IleCavallo",
          "Corse-IleLavezzu",
          "Corse-ArchipelDesSanguinaires",
          "Corse-IlePinarellu",
          "Corse-IleCerbicale",
          "Corse-IleDeLaPietra",
          "Corse-IleDePiana",
          "Corse-IleDePietricaggiosa",
          "Corse-IleDeForana",
          "Corse-PrequIleParata",
          "Corse-IleCapense",
          "Corse-IleDeLaGiraglia"
          ]

aLaReunion = ["LaReunion"]

aAntilles = ["Antilles-Martinique",
             "Antilles-Martinique-IletChancel",
             "Antilles-Martinique-IletsOscarThierry",
             "Antilles-Martinique-IletAChevalier",
             "Antilles-Martinique-RocherDuDiamand",
             "Antilles-Martinique-GrosIlet",
             "Antilles-Martinique-IleDeLaPetiteGrenade",
             "Antilles-Martinique-IletLong",
             "Antilles-Martinique-IleMetrente",
             "Antilles-Martinique-IletLavigne",
             "Antilles-Guadeloupe-BasseTerre",
             "Antilles-Guadeloupe-GrandeTerre",
             "Antilles-Guadeloupe-IletACochons",
             "Antilles-Guadeloupe-IletsPigeon",
             "Antilles-Guadeloupe-IletAKahouanne",
             "Antilles-IleDeLaPetiteTerre",
             "Antilles-IletAFayou",
             "Antilles-MarieGalante",
             "Antilles-IleDesSaintes-TerreDeHaut",
             "Antilles-IleDesSaintes-TerreDeBas",
             "Antilles-IleDesSaintes-IletACabrit",
             "Antilles-IleSaintMartin-Francaise",
             "Antilles-IleSaintMartin-TerresBasses",
             "Antilles-IleSaintMartin-Marigot1",
             "Antilles-IleSaintMartin-PointeDuBluff",
             "Antilles-IleSaintMartin-IletDePinel",
             "Antilles-LaDesirade",
             "Antilles-IleTintamarre",
             "Antilles-GrandIlet"
             ]

aMayotte = ["Mayotte-GrandeTerre",
            "Mayotte-PetiteTerre",
            "Mayotte-Mtsambro",
            "Mayotte-IlotMbouzi",
            "Mayotte-PrequilHandrema-Nord",
            "Mayotte-IlotHandrema-Ouest",
            "Mayotte-PointeBandraboua",
            "Mayotte-IlotPamandziKeli",
            "Mayotte-PresquilDzagudzi-Ouest",
            "Mayotte-IlotBrandrele",
            "Mayotte-IlotKaroni",
            "Mayotte-IlotDeSableBlanc"
            ]

aGuyane = ["Guyane-Francaise",
           "Guyane-Francaise-Awala",
           "Guyane-Francaise-IletDeRemire",
           "Guyane-Francaise-IlesRemire",
           "Guyane-Francaise-IleRoyale",
           "Guyane-Francaise-IletLesMamellesOuest",
           "Guyane-Francaise-IleSaintJoseph",
           "Guyane-Francaise-IleDuDiableNord"
           ]

iDelta = len(oFranceNames) - (len(aFrance)+len(aCorse)+len(aLaReunion)+len(aAntilles)+len(aMayotte)+len(aGuyane))
if iDelta != 0:
    sErr = "Erreur de répartition dans les tableaux. Delta zone=" + str(iDelta)
    oLog.error(sErr, outConsole=True)
    bpaTools.sysExitError(sErr)
