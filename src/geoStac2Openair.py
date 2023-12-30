#!/usr/bin/env python3

from bs4 import BeautifulSoup
try:
    import bpaTools
except ImportError:
    ### Include local modules/librairies  ##
    import os
    import sys
    from time import gmtime, strftime
    aixmParserLocalSrc  = "../../aixmParser/src/"
    module_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(module_dir, aixmParserLocalSrc))
    import bpaTools


class GeoStac:

    def __init__(self)-> None:
        self.appPath = bpaTools.getFilePath(__file__)
        #self.inputPath = self.appPath + "../input/_geoRef/"
        self.appVersion = bpaTools.getVersionFile()                 #Your app version

    #Extrait d'un KML
    ### Modele --> 20240229_ZSM-tempon-france.kml
    #   <Placemark>
    #       <Style><LineStyle><color>ff0000ff</color></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style>
    #   	<ExtendedData><SchemaData schemaUrl="#zsm_tampon__kml__10__2023__ktgmg">
    #   	<SimpleData name="id_zsm_tampon">5498</SimpleData>
    #   	<SimpleData name="code_zsm">ZSM T-06 SEC 1044 | N-23-0000105 | Rocher du Prêtre 1 - (5498)</SimpleData>
    #   	<SimpleData name="actif">1</SimpleData>
    #   	<SimpleData name="cd_nom">2852</SimpleData>
    #   	<SimpleData name="espece">Gypaète barbu</SimpleData>
    #   	<SimpleData name="nom_latin">Gypaetus barbatus (Linnaeus, 1758)</SimpleData>
    #   	<SimpleData name="equivalence_code_reseau">N-23-0000105</SimpleData>
    #   	<SimpleData name="nom_aire">Rocher du Prêtre 1</SimpleData>
    #   	<SimpleData name="aire_historique">0</SimpleData>
    #   	<SimpleData name="code_dep">06</SimpleData>
    #   	<SimpleData name="code_aire">06 SEC 1044</SimpleData>
    #   	<SimpleData name="idcode_aire">4673</SimpleData>
    #   	<SimpleData name="site">23</SimpleData>
    #   	<SimpleData name="idsite">65</SimpleData>
    #   	<SimpleData name="structure">(49:142,38,91,216,39,33,34,93,54,41,217,85,88,129,103,137,118,94,218,220,26,30,144,130,126,56,222,164,187,188,209,210,211,190,215,186,132,189,256,268,259,234,235,261,155,263,254,258,144)</SimpleData>
    #   	<SimpleData name="acces_util">(53:1007,255,586,596,971,713,1004,448,782,1005,695,828,1006,563,530,220,536,457,470,663,637,471,217,370,444,978,600,532,692,625,686,621,687,674,914,214,722,253,589,595,573,541,331,980,587,953,964,932,746,728,225,920,625)</SimpleData>
    #   	<SimpleData name="acces_util_not">(28:282,437,883,781,776,822,831,904,252,280,522,376,548,281,535,406,294,299,475,377,639,963,959,965,989,833,967,968)</SimpleData>
    #   	<SimpleData name="idespece">9</SimpleData>
    #   	<SimpleData name="geom">POLYGON((1007727.5455325 6363548.0641425,1007568.0482443 6363414.0864203,1007360.7017695 6363340.7176677,1007178.8748609 6363369.4271796,1007070.4167049 6363452.3657695,1006773.7517487 6363493.8350644,1006611.0645147 6363481.0752814,1006457.9471179 6363481.0752814,1006225.0810771 6363452.3657695,1005813.5780733 6363375.8070711,1005504.1533341 6363350.287505,1005478.633768 6363414.0864203,1006671.6734842 6364186.0532955,1006212.8673768 6365114.8114942,1008630.8463069 6366429.0691712,1009456.4961373 6364020.1761157,1009271.4792829 6363860.6788275,1008997.1439471 6363790.5000206,1008792.9874181 6363697.9915934,1008576.0711061 6363605.4831662,1008384.6743602 6363554.444034,1008131.59586994 6363491.42394497,1007985.9311395 6363509.7847933,1007727.5455325 6363548.0641425))</SimpleData>
    #   	</SchemaData></ExtendedData>
    #   	<Polygon><outerBoundaryIs><LinearRing><coordinates>6.85876246870407,44.303271175482 6.85668363564878,44.3021367472755 6.85404291985552,44.3015682080127 6.85178412697944,44.3019061538178 6.85047697432734,44.3026994204734 6.84678817396846,44.3032023598887 6.84474359728236,44.3031589345735 6.84282661553173,44.303226000057 6.83989370417719,44.3030698125484 6.83469521352875,44.3025614289196 6.83080581276732,44.3024671283453 6.83052509508894,44.3030518684346 6.84593262324004,44.3094706176594 6.84075395536067,44.3180217725073 6.87184133974838,44.3287753454983 6.88069863811384,44.306753333046 6.87828402956329,44.3054011622424 6.87480621895506,44.3048914011066 6.87219337027232,44.3041498129312 6.86942084338355,44.3034137890876 6.8669933233836,44.3030392831895 6.86378627072408,44.3025841679444 6.86197388562774,44.3028133605007 6.85876246870407,44.303271175482</coordinates></LinearRing></outerBoundaryIs></Polygon>
    #   </Placemark>
    ### Modele --> 20240229_ZSM-coeur-france.kml
    #   <Placemark>
    #       <Style><LineStyle><color>ff0000ff</color></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style>
    #       <ExtendedData><SchemaData schemaUrl="#zsm_coeur__kml__11__2023__fdbj8">
    #       <SimpleData name="id_zsm_coeur">4505</SimpleData>
    #       <SimpleData name="code_zsm">ZSM C-65 LU 062 | D2 - Gavarnie-Ossoue PNPY_65_LU_D2_062  | Ossoue Carrière - (4505)</SimpleData>
    #       <SimpleData name="actif">1</SimpleData>
    #       <SimpleData name="cd_nom">2852</SimpleData>
    #       <SimpleData name="espece">Gypaète barbu</SimpleData>
    #       <SimpleData name="nom_latin">Gypaetus barbatus (Linnaeus, 1758)</SimpleData>
    #       <SimpleData name="equivalence_code_reseau">D2 - Gavarnie-Ossoue PNPY_65_LU_D2_062 </SimpleData>
    #       <SimpleData name="nom_aire">Ossoue Carrière</SimpleData>
    #       <SimpleData name="aire_historique">0</SimpleData>
    #       <SimpleData name="code_dep">65</SimpleData>
    #       <SimpleData name="code_aire">65 LU 062</SimpleData>
    #       <SimpleData name="idcode_aire">3272</SimpleData>
    #       <SimpleData name="site">D2</SimpleData>
    #       <SimpleData name="idsite">14</SimpleData>
    #       <SimpleData name="structure">(73:142,38,91,80,84,82,75,23,67,216,33,7,34,93,54,139,170,41,171,16,217,85,88,96,128,87,89,90,97,103,137,105,92,118,110,94,218,220,26,57,30,130,126,56,221,222,145,134,164,138,187,174,209,210,211,190,215,183,186,189,191,202,199,17,256,234,269,270,243,263,254,258,7)</SimpleData>
    #       <SimpleData name="acces_util">(153:1007,255,853,468,676,441,216,596,568,442,31,888,60,185,446,930,585,969,982,761,118,353,713,832,860,583,448,776,974,897,871,695,730,71,828,1006,902,675,6,670,451,220,536,440,457,109,110,30,479,61,663,637,461,115,52,662,56,64,58,666,53,54,57,68,248,218,211,249,217,112,909,105,107,121,130,117,29,43,223,292,120,642,444,97,227,82,978,447,600,63,686,219,85,98,102,32,257,435,192,684,705,687,917,918,561,674,914,915,916,476,549,42,251,445,214,376,722,539,253,706,210,589,245,204,381,114,620,595,629,604,627,651,597,573,541,86,906,452,378,377,38,639,980,938,428,953,964,989,746,728,225,391,102)</SimpleData>
    #       <SimpleData name="acces_util_not">(71:1008,1010,1011,282,437,273,883,244,607,825,781,973,822,782,823,900,506,831,279,904,252,269,280,505,522,548,426,281,535,503,634,510,565,274,544,284,576,267,406,511,542,294,508,247,256,504,502,518,259,495,545,299,4,475,278,268,507,425,509,661,948,266,963,959,965,990,920,833,967,968,193)</SimpleData>
    #       <SimpleData name="idespece">9</SimpleData>
    #       <SimpleData name="geom">POLYGON((452829.2076 6187770.633,452876.4912 6187717.138,452897.6148 6187655.618,452886.2502 6187582.235,452870.5704 6187540.59,452842.3122 6187500.308,452809.5798 6187472.653,452747.1474 6187438.031,452643.5208 6187418.171,452493.8952 6187399.607,452125.2546 6187219.759,452051.5512 6187192.327,451966.377 6187147.937,451813.5936 6187121.158,451728.9072 6187121.971,451661.1366 6187133.861,451283.9352 6187261.84,451160.65848068 6187349.9253775,451091.02575797 6187450.8926483,450980.4876 6187492.673,450859.626 6187561.768,450786.429 6187595.678,450690.4056 6187748.231,450692.6934 6188025.41,450726.8258566 6188278.1995952,450803.8164 6188468.102,450886.32314487 6188699.2724362,451022.19562923 6188879.6700914,451207.21248362 6188866.9103084,451376.27960918 6188822.2510677,451507.06738556 6188831.820905,451569.51761882 6188801.8346688,451612.5818863 6188742.8206726,451639.69642508 6188671.0468935,451682.51440265 6188614.9045929,451723.6764 6188595.676,451893.29711133 6188557.8038198,452075.7282 6188471.223,452271.8514 6188327.228,452431.9788 6188189.939,452506.9044 6188101.995,452581.824 6187999.516,452829.2076 6187770.633))</SimpleData>
    #       </SchemaData></ExtendedData>
    #       <Polygon><outerBoundaryIs><LinearRing><coordinates>-0.016110266246654,42.747004638833 -0.015508930549356,42.7465402278085 -0.01522276996075,42.7459947310366 -0.015327132172738,42.7453314950899 -0.015498877300832,42.7449519388701 -0.015824587815432,42.7445803104574 -0.016210717503384,42.7443205963352 -0.016955641705562,42.7439880836178 -0.018209594441047,42.743774046681 -0.020024866828729,42.7435558262696 -0.024434546105537,42.7418130974478 -0.025320138124943,42.7415412470991 -0.026337617902716,42.7411130740973 -0.02818742620163,42.74081981821 -0.029220074215568,42.7407979237663 -0.030051713721805,42.7408813785207 -0.034709508921052,42.7419010226478 -0.036253494898364,42.7426498461173 -0.037149654329468,42.7435329376904 -0.038516701042775,42.743870095475 -0.040022431067574,42.7444490779106 -0.040930628480366,42.7447284142221 -0.042172838396738,42.7460658130123 -0.04227519650086,42.7485569869574 -0.041977873083331,42.7508400620106 -0.041128465678317,42.7525729519715 -0.040231135518277,42.7546785326319 -0.038659239802914,42.7563463877064 -0.036397435246321,42.7562957218349 -0.03431514861271,42.7559528869711 -0.032725009257483,42.7560840372087 -0.031949540933495,42.7558361735159 -0.031396846535901,42.7553208041051 -0.031032649854268,42.7546852838795 -0.030484321672935,42.7541956270779 -0.029973470424172,42.7540370606121 -0.027887727748794,42.7537552732312 -0.025623055566004,42.7530402174358 -0.023164695782348,42.7518139681214 -0.021148407994039,42.7506355370289 -0.020193931043142,42.7498711378455 -0.019232773631476,42.7489761337565 -0.016110266246654,42.747004638833</coordinates></LinearRing></outerBoundaryIs></Polygon>
    #   </Placemark>
    #Utilitaire pour construction d'un format Openair sur la base de données KML
    def geoStacKml2Openair(self, sPath:str="", sFile:str="") -> None:
        def coord2Openair(aPol:list) -> None:
            for oPoint in aPol:
                #oDmsPoint = bpaTools.GeoCoordinates.geoStr2coords(oPoint[1], oPoint[0], "dms", ":", " ")           #For native coords with decimals values
                oDmsPoint = bpaTools.GeoCoordinates.geoStr2coords(oPoint[1], oPoint[0], "dms", ":", " ", digit=0)   #For Control with 'Friend Air Tools' - https://mids.be/fat/
                sPoint = "DP " + " ".join(oDmsPoint)
                aPoints.append(sPoint)

        def makeOpenairHead(oPlacemark) -> None:
            sMsg:str = ""

            sZsmType:str    = "Zone "
            oId             = oPlacemark.find("SimpleData", attrs={"name":"id_zsm_tampon"})
            if oId:
                sZsmType    += "Tampon"
            else:
                oId         = oPlacemark.find("SimpleData", attrs={"name":"id_zsm_coeur"})
                if oId:
                    sZsmType += "Coeur"
                else:
                    sMsg = "(!)Warning --> " + oPlacemark.text
                    print(sMsg)
                    return

            oCode           = oPlacemark.find("SimpleData", attrs={"name":"code_zsm"})
            oEspece         = oPlacemark.find("SimpleData", attrs={"name":"espece"})
            oIdEspece       = oPlacemark.find("SimpleData", attrs={"name":"idespece"})
            #oActif          = oPlacemark.find("SimpleData", attrs={"name":"actif"})
            #oNom            = oPlacemark.find("SimpleData", attrs={"name":"cd_nom"})
            #oNomAir         = oPlacemark.find("SimpleData", attrs={"name":"nom_aire"})

            sID:str         = "LFZSMDSTAC" + oId.text
            sAltM:str       = "300m/sol"    # 300m ou 600m  --> Le 30/12/2023, Pierre SpotAir en référence au dialogue avec la FFVL ; me confirme de rester sur la base des 300m/sol
            sAltF:str       = "985FT AGL"   # 300m=985FT ou 600m=1969FT
            sActiv:str      = ""
            sTimes          = ""
            sIdEspece       = oIdEspece.text

            if sIdEspece == "9":            #Gypaète barbu
                #Gypaète barbu --> L’ensemble des ZSM* est activé à la date du 1er novembre pour le Gypaète barbu. Elles sont maintenues jusqu’à l’émancipation du jeune en cas de reproduction réussie, soit le 15 août au 31 août pour les Alpes.
                sActiv = '[TIMSH] Survol interdit à moins de ' + sAltM + '; période: 1=(01/01->31/08) 2=(01/11->31/12)'
                sTimes = '{"1": ["UTC(01/01->31/08)", "ANY(00:00->23:59)"], "2": ["UTC(01/11->31/12)", "ANY(00:00->23:59)"]}'
            elif sIdEspece == "???":            #Vautour percnoptère
                #Vautour percnoptère --> L’ensemble des ZSM* est activé à la date du 1er mars pour le Vautour percnoptère. Elles sont maintenues jusqu’à l’émancipation du ou des jeunes en cas de reproduction réussie, soit le 15 septembre
                sActiv = '[TIMSH] Survol interdit à moins de ' + sAltM + '; période: 1=(01/03->15/09)'
                sTimes = '{"1": ["UTC(01/03->15/09)", "ANY(00:00->23:59)"]}'
            elif sIdEspece == "???":            #Vautour moine
                #Vautour moine --> L’ensemble des ZSM non historiques est activé à la date du 15 Décembre. Elles sont maintenues jusqu’à l’émancipation du jeune, soit le 15 octobre
                sActiv = '[TIMSH] Survol interdit à moins de ' + sAltM + '; période: 1=(01/01->15/10) 2=(15/12->31/12)'
                sTimes = '{"1": ["UTC(01/01->15/10)", "ANY(00:00->23:59)"], "2": ["UTC(15/12->31/12)", "ANY(00:00->23:59)"]}'
            else:
                sMsg = " (!)Warning - Espece id=" + sIdEspece
                sActiv = sMsg
                sTimes = sMsg
                print(sMsg)

            sName:str = oId.text + " " + oEspece.text + " - " + sZsmType + " " + sAltM + " (BIRD)"
            sDesc:str = oCode.text

            sDesc = sDesc.replace("\u2009", " ")   #for UnicodeEncodeError: 'charmap' codec can't encode character '\u2009'
            sDesc = sDesc.replace("&apos;","'")
            sDesc = sDesc.replace("&quot;",'"')
            sDesc = sDesc.replace("\n"," ")
            sDesc = sDesc.replace("  "," ")
            sDesc = sDesc.replace(" :",":")
            sDesc = sDesc.replace(" ;",";")
            sDesc = sDesc.replace(" ,",",")
            sDesc = sDesc.replace(" .",".")
            #sDesc = sDesc.replace("#"," ")         #SIA spécifique

            aPoints.append("AC ZSM")
            aPoints.append("AY PROTECT")
            aPoints.append("AN PROTECT " + sName)
            aPoints.append("*AUID GUId=! UId=! Id=" + sID)
            aPoints.append("*ADescr [Pascal Bazile (c) " + strftime("%m/%Y", gmtime()) + "] " + sDesc + " [source - https://parapente.ffvl.fr/harmonie-rapaces]")
            aPoints.append("*AActiv " + sActiv)
            aPoints.append("*ATimes " + sTimes)
            aPoints.append("AH " + sAltF)
            aPoints.append("AL SFC")

            #   <coordinates>-0.016110266246654,42.747004638833 -0.015508930549356,42.7465402278085 -0.01522276996075,42.7459947310366 -0.015327132172738,42.7453314950899 -0.015498877300832,42.7449519388701 -0.015824587815432,42.7445803104574 -0.016210717503384,42.7443205963352 -0.016955641705562,42.7439880836178 -0.018209594441047,42.743774046681 -0.020024866828729,42.7435558262696 -0.024434546105537,42.7418130974478 -0.025320138124943,42.7415412470991 -0.026337617902716,42.7411130740973 -0.02818742620163,42.74081981821 -0.029220074215568,42.7407979237663 -0.030051713721805,42.7408813785207 -0.034709508921052,42.7419010226478 -0.036253494898364,42.7426498461173 -0.037149654329468,42.7435329376904 -0.038516701042775,42.743870095475 -0.040022431067574,42.7444490779106 -0.040930628480366,42.7447284142221 -0.042172838396738,42.7460658130123 -0.04227519650086,42.7485569869574 -0.041977873083331,42.7508400620106 -0.041128465678317,42.7525729519715 -0.040231135518277,42.7546785326319 -0.038659239802914,42.7563463877064 -0.036397435246321,42.7562957218349 -0.03431514861271,42.7559528869711 -0.032725009257483,42.7560840372087 -0.031949540933495,42.7558361735159 -0.031396846535901,42.7553208041051 -0.031032649854268,42.7546852838795 -0.030484321672935,42.7541956270779 -0.029973470424172,42.7540370606121 -0.027887727748794,42.7537552732312 -0.025623055566004,42.7530402174358 -0.023164695782348,42.7518139681214 -0.021148407994039,42.7506355370289 -0.020193931043142,42.7498711378455 -0.019232773631476,42.7489761337565 -0.016110266246654,42.747004638833</coordinates>
            oCords          = oPlacemark.find("coordinates", recursive=True)
            sCoords:str     = oCords.text
            aCoords:list    = sCoords.split(" ")
            aKmlPolygon:list = []
            for oPoint in aCoords:
                aPoint = oPoint.split(",")
                aKmlPolygon.append((float(aPoint[0]), float(aPoint[1])))
            coord2Openair(aKmlPolygon)
            aPoints.append("")

        aKmlPolygon:list = None
        aPoints:list = []
        if sFile:
            oKml = BeautifulSoup(open(sPath + sFile, encoding="utf-8"), "xml", from_encoding="utf-8")
            aPoints.append("**************************************************")
            aPoints.append("*   software - (GeoRef.GeoStac v" + self.appVersion + ") Paragliding-OpenAir-French-Files - http://pascal.bazile.free.fr/paraglidingFolder/divers/GPS/OpenAir-Format/")
            aPoints.append("*   created - " + bpaTools.getNowISO())
            aPoints.append("*   srcFile - " + sFile + " - content: " + oKml.find("Schema").attrs["name"])
            aPoints.append("**************************************************")
            aPoints.append("")
            oList = oKml.find_all("Placemark", recursive=True)
            idx = 0
            for oPlacemark in oList:
                idx+=1
                makeOpenairHead(oPlacemark)

            sFileDst = sFile.replace(".kml", ".txt")
            bpaTools.writeTextFile(sPath + sFileDst, "\n".join(aPoints))
            print(sPath + sFileDst);
        return


if __name__ == '__main__':
    o = GeoStac()
    o.geoStacKml2Openair("D:\_Users_\BPascal\_4_Src\GitHub\poaff\input\STAC/", "20240229_ZSM-coeur-france.kml")
