#!/usr/bin/env python3

try:
    import bpaTools
except ImportError:
    ### Include local modules/librairies  ##
    import os
    import sys
    from time import gmtime, strftime
    import unidecode
    from bs4 import BeautifulSoup
    aixmParserLocalSrc  = "../../aixmParser/src/"
    module_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(module_dir, aixmParserLocalSrc))
    import bpaTools

class GeoBiodivSports:

    def __init__(self)-> None:
        self.appPath = bpaTools.getFilePath(__file__)
        #self.inputPath = self.appPath + "../input/_geoRef/"
        #self.appVersion = bpaTools.getVersionFile()                 #or your app version

    def geoJsonBiodivSports2Openair(self, sYersFilter:list, sPath:str="", sFileSrc:str="") -> None:
        #Procédure: 	https://biodiv-sports.fr/api/v2/
        #   ouvrir sensitivearea
        #   cliquer GET /api/v2/sensitivearea/
        #   cliquer Parameters --> 'Try it Out'
        #       language = fr
        #       format = geojson
        #   cliquer Execute
        #   cliquer Download
        #   Enregistrer le fichier sous format type 'YYYYMMDD_LPO_All_Parcs-et-ZSMs.geojson'
        oLPOdata:dict = bpaTools.readJsonFile(sPath + sFileSrc)         #encoding="utf-8"
        aNewFeatParc:list = []
        aNewFeatActZsm:list = []
        aNewFeatNotActZsm:list = []
        aNewFeatOthers:list = []
        for aFeat in oLPOdata["features"]:
            oProps = aFeat["properties"]
            sName = oProps["name"]
            aPractices = oProps["practices"]                            # https://biodiv-sports.fr/api/v2/sportpractice/ --> practices parameter --> 1=Terrestre; 2=Vertical; 3=Aerien; 4=?, 5=Aquatique; 6=Souterrain; 7=Oiseaux?
            #sCreaDT = oProps["create_datetime"]                        # "2021-03-26T10:55:53.379470+01:00"
            sUpdtDT = oProps["update_datetime"]                         # "2022-03-22T10:59:54.076878+01:00"
            sStruct = oProps["structure"]

            bValid:bool = (3 in aPractices) or (7 in aPractices)        #Pratique "aérienne" ou "autres"

            bZSM:bool = False
            bZSM = bZSM or sStruct[:3]=="LPO"                           #Ligue Protection Oiseaux
            bZSM = bZSM or ("Gypaète barbu".lower() in sName.lower())
            bZSM = bZSM or ("Aigle royal".lower() in sName.lower())
            bZSM = bZSM or ("Faucon pèlerin".lower() in sName.lower())
            bZSM = bZSM or ("Vautour fauve".lower() in sName.lower())
            bZSM = bZSM or ("Grand tétras".lower() in sName.lower())
            bZSM = bZSM or ("Tétras lyre".lower() in sName.lower())
            bZSM = bZSM or ("Circaète".lower() in sName.lower())
            bZSM = bZSM or ("Zone de quiétude".lower() in sName.lower())
            bZSM = bZSM or ("Zone de protection renforcée".lower() in sName.lower())
            bZSM = bZSM or ("Zone de Recherche".lower() in sName.lower())

            if bValid and bZSM and sUpdtDT[:4] in sYersFilter:
                aNewFeatActZsm.append(aFeat)
            elif bValid and bZSM:
                aNewFeatNotActZsm.append(aFeat)

            bParc:bool = False
            if not bZSM:
                bParc = bParc or sStruct[:2]=="PN"                                                  #Parc National
                bParc = bParc or sStruct[:3]=="PNR"                                                 #Parc National Régional
                bParc = bParc or sStruct[:3]=="RNF"                                                 #Réserve Naturelle Nationale
                bParc = bParc or sStruct[:6]=="Asters"                                              #Réserve Naturelle Nationale
                bParc = bParc or ("Parc National".lower() in sStruct.lower())                       #Parc National
                bParc = bParc or ("Pyrénées-Orientales".lower() in sStruct.lower())                 #Autres Parcs
                bParc = bParc or ("Conservatoire d'espaces naturels".lower() in sStruct.lower())    #Réserve Naturelle
                bParc = bParc or ("Réserve Naturelle ".lower() in sName.lower())                    #Réserve Naturelle
                bParc = bParc or ("Réserve de chasse".lower() in sName.lower())                     #Réserve de chasse

                if bValid and bParc:
                    aNewFeatParc.append(aFeat)
                else:
                    print(sStruct)

            if (not bParc) and (not bZSM):
                aNewFeatOthers.append(aFeat)

        if len(aNewFeatActZsm)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatActZsm})
            sFileDst = sFileSrc.replace(".geojson","_Zsm-Active.txt")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson, ensure_ascii=True)
            self.geoJson2Openair1("ZSM", sPath, sFileDst)

        if len(aNewFeatNotActZsm)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatNotActZsm})
            sFileDst = sFileSrc.replace(".geojson","_Zsm-OLD.txt")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson, ensure_ascii=True)
            self.geoJson2Openair1("ZSM", sPath, sFileDst)

        if len(aNewFeatParc)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatParc})
            sFileDst = sFileSrc.replace(".geojson","_Parc.txt")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson, ensure_ascii=True)
            self.geoJson2Openair1("GP", sPath, sFileDst)

        if len(aNewFeatOthers)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatOthers})
            sFileDst = sFileSrc.replace(".geojson","_Warning-Others.txt")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson, ensure_ascii=True)
            self.geoJson2Openair1("P", sPath, sFileDst)
        return

    def geoJson2Openair1(self, sClassType:str, sPath:str="", sFile:str="", bZSM:bool=False, bParc:bool=False) -> None:
        def coord2Openair(aPol:list) -> None:
            for oPoint in aPol:
                oDmsPoint = bpaTools.GeoCoordinates.geoStr2coords(oPoint[1], oPoint[0], "dms", ":", " ")    #For native coords with decimals values
                #oDmsPoint = bpaTools.GeoCoordinates.geoStr2coords(oPoint[1], oPoint[0], "dms", ":", "", digit=0)    #For Control with 'Friend Air Tools' - https://mids.be/fat/
                sPoint = "DP " + " ".join(oDmsPoint)
                aPoints.append(sPoint)

        def makeOpenairHead(aFeat:dict) -> bool:
            #Ne pas intégrer certaines zones posant problème car déjà tracé par BPascal et avec protocoles ou caractéristiques particulières
            aFilter:list = []
            aFilter.append("Réserve naturelle nationale des Aiguilles Rouges")
            aFilter.append("Réserve naturelle nationale du Bout du Lac d'Annecy")
            aFilter.append("Réserve naturelle nationale du Roc de Chère")
            aFilter.append("Réserve Nationale de Chasse et de Faune Sauvage des Bauges")
            aFilter.append("Parapentes et delta-planes - Secteur V1 dit de la Turra")
            aFilter.append("Parapentes et delta-planes - Secteur V2 dit de la Dent Parrachée")
            aFilter.append("Parapentes et delta-planes - Secteur V3 dit du Barbier")
            aFilter.append("Parapentes et delta-planes - Secteur V4 dit de la Loza")
            aFilter.append("Parapentes et delta-planes - Secteur V5 dit des Adrets de Val Cenis")
            aFilter.append("Parapentes et delta-planes - Secteur V6 dit des Adrets de Bessans A")
            aFilter.append("Parapentes et delta-planes - Secteur V6 dit des Adrets de Bessans B")
            aFilter.append("Parapentes et delta-planes - secteur V7 dit du Barbier ouest")
            aFilter.append("Parapentes et delta-planes - secteur V8 dit de la Grande Feiche")
            aFilter.append("Planeurs secteur P1")
            aFilter.append("Planeurs secteur P2")
            aFilter.append("Coeur du Parc national des Pyrénées")
            aFilter.append("La Caume")

            ### source Biodiv-sport --> Properties: {
            ###     'contact': 'LPO BFC - DT Sa&ocirc;ne-et-Loire<br />Mail : saone-et-loire@lpo.fr<br />Tel : 03 85 48 77 70<br />Site : <a href="https://bfc.lpo.fr/">https://bfc.lpo.fr/<br /><img src="https://bourgogne-franche-comte.lpo.fr/wp-content/uploads/2023/01/cropped-LPO-BFC-logo-signature-droite.png" alt="" width="200" height="83" /></a>',
            ###     'create_datetime': '2023-01-17T14:46:15.131484+01:00',
            ###     'description': "FR3800975 &ndash; Basse Vall&eacute;e du Doubs<br />Esp&egrave;ces concern&eacute;es : Sterne pierregarin, &OElig;dicn&egrave;me criard, Petit gravelot, Gu&ecirc;pier d&rsquo;Europe, Hirondelle de rivage, Gorgebleue &agrave; miroir, Bruant proyer, Chev&ecirc;che d&rsquo;Ath&eacute;na, Courlis cendr&eacute;, Huppe fasci&eacute;e, Pie-gri&egrave;che &eacute;corcheur, Tarier des pr&eacute;s, Castor d&rsquo;Europe, L&eacute;zard des souches, Cuivr&eacute; des marais, Gratiole officinale.<br /><br />Afin de garantir l'&eacute;quilibre biologique des milieux n&eacute;cessaires &agrave; la reproduction, l'alimentation, le repos et la survie de l'esp&egrave;ce concern&eacute;e, il est instaur&eacute; un arr&ecirc;t&eacute; pr&eacute;fectoral de protection de biotope sur la Basse Vall&eacute;e du Doubs.<br /><br />Dans ce p&eacute;rim&egrave;tre, est interdit pendant la p&eacute;riode de reproduction (du 01/03 au 31/07) :<br /><br />&nbsp; &nbsp;- Le survol &agrave; moins de 150 m du sol part tout a&eacute;ronef, y compris engins volant t&eacute;l&eacute;guid&eacute;<br />&nbsp; &nbsp;- L&rsquo;accostage d&rsquo;engins nautique et le d&eacute;barquement<br />&nbsp; &nbsp;- La divagation des chiens<br />&nbsp; &nbsp;- La circulation &agrave; pied<br /><br />Merci d'&eacute;viter le secteur pour permettre la reproduction de l'esp&egrave;ce.",
            ###     'elevation': 150,
            ###     'info_url': 'https://inpn.mnhn.fr/espace/protege/FR3800975',
            ###     'kml_url': 'https://biodiv-sports.fr/api/fr/sensitiveareas/1506.kml',
            ###     'openair_url': 'https://biodiv-sports.fr/api/fr/sensitiveareas/1506/openair',
            ###     'name': 'APPB Basse Vallée du Doubs',
            ###     'period': [False, False, True, True, True, True, True, False, False, False, False, False],
            ###     'practices': [3, 5, 1],
            ###     'published': True,
            ###     'species_id': None,
            ###     'structure': 'LPO',
            ###     'update_datetime': '2023-03-08T21:53:33.895056+01:00',
            ###     'url': 'https://biodiv-sports.fr/api/v2/sensitivearea/1506/?format=geojson'}

            if str(aFeat["properties"].get("name","")) in aFilter:
                return False

            sNameTmp:str = aFeat["properties"].get("name","")
            sWarning:str = ""
            lElevation:int = aFeat["properties"].get("elevation",None)
            #if "Mercantour" in sNameTmp:
            #    0==1
            if (lElevation == 0) or (lElevation is None):
                if   "Vautour fauve" in sNameTmp:               lElevation = 150
                elif "Aigle royal" in sNameTmp:                 lElevation = 150
                elif "Lagopède alpin" in sNameTmp:              lElevation = 150
                elif "Gypaete barbu" in sNameTmp:               lElevation = 300
                elif "Vautour percnoptère" in sNameTmp:         lElevation = 300
                elif "d'Ossau" in sNameTmp:                     lElevation = 500
                elif "Bout du Lac d'Annecy" in sNameTmp:        lElevation = 200
                elif "Habert de la Dame" in sNameTmp:           lElevation = 300
                elif "Massif des Voirons" in sNameTmp:          lElevation = 300
                elif "Massif duVuache" in sNameTmp:             lElevation = 300
                elif "Massif du Vuache" in sNameTmp:            lElevation = 300
                elif "Mercantour" in sNameTmp:                  lElevation = 1000
                elif "Haute-Chaîne du Jura" in sNameTmp:        lElevation = 150
                elif "Sixt-Fer-à-Cheval-Passy" in sNameTmp:     lElevation = 300
                elif "Aiguilles Rouges" in sNameTmp:            lElevation = 300
                elif "Quié de Lujat" in sNameTmp:               lElevation = 500
                elif "Roc de Sédour" in sNameTmp:               lElevation = 200
                elif "falaises de Sourroque" in sNameTmp:       lElevation = 200
                elif "faune sauvage de Casteil" in sNameTmp:    lElevation = 300
                elif "gorges de Péreille" in sNameTmp:          lElevation = 200
                elif "Montagne de Chevran" in sNameTmp:         lElevation = 200
                elif "Côte de la Baume" in sNameTmp:            lElevation = 150
                elif "Col Ratti" in sNameTmp:                   lElevation = 150
                elif "Roselières du Léman" in sNameTmp:         lElevation = 300
                else:
                    sWarning = " - (/!\Warning - Default ceiling affected)"
                    lElevation = 300
                    return False                                    #BPascal le 27/09/2023 - Sortie volontaire sans prise en compte de cette zone qui n'est pas décrit avec une altitude altitude

            aPoints.append("AC " + sClassType)

            sType:str=""
            sExt:str = ""
            sName:str = "AN "
            if sClassType == "ZSM":
                sType = "PROTECT"
                sExt = " (BIRD)"
                sName += sType
            elif sClassType == "GP":
                sType = "PROTECT"
                sExt = " (FAUNA)"
                sName += sType
            elif sClassType == "P":
                sName += sClassType

            if sType!="":
                aPoints.append("AY " + sType)

            sAlt:str = str(lElevation) + "m/sol"                    #BPascal - 984 pieds = 300 mètres de plafond par défaut
            sFeet:str = str(int(lElevation / 0.3048) + 1)           #Conversion des mètres en pieds

            sID:str = ""
            if "name" in aFeat["properties"]:
                sID += aFeat["properties"].get("name","")
                sName += " " + sID + " " + sAlt + sExt
            else:
                sID += "{Autoload}-" + str(lFeatNumber) + "." + str(lSubFeatNumber)
                sName += " Autoload " + sID + " " + sAlt+ sExt

            aPoints.append(sName)

            sID = "LF" + unidecode.unidecode(sID.replace(" ","")) + "-" + str(lFeatNumber) + "." + str(lSubFeatNumber)
            aPoints.append("*AUID GUId=! UId=! Id=" + sID)

            sDesc:str = "*ADescr [Pascal Bazile (c) " + strftime("%m/%Y", gmtime())
            sDesc += " / (Update) " + aFeat["properties"].get("update_datetime","")[:10]
            sDesc += " https://biodiv-sports.fr + " + aFeat["properties"].get("structure","") + "] "
            if aFeat["properties"]["description"]:
                ##OLD src
                #sDesc += " - " + aFeat["properties"].get("description","")
                #sDesc = sDesc.replace("<br />","<br/>")
                #sDesc = sDesc.replace("<br/>","")
                #sDesc = sDesc.replace("<strong>","")
                #sDesc = sDesc.replace("</strong>","")
                sTmpDesc:str = "<a>" + str(aFeat["properties"].get("description","")) + "</a>"
                soup = BeautifulSoup(sTmpDesc, features="lxml")  #from_encoding='utf-8'
                sTmp:str = str(soup.get_text()).replace("\t"," ")
                sTmp = sTmp.replace("\n"," ")
                sTmp = sTmp.replace("\r"," ")
                sTmp = sTmp.replace("  "," ")
                sDesc += sTmp
            if aFeat["properties"]["info_url"]:
                sDesc += " - (Source) " + aFeat["properties"].get("info_url","")
            sDesc += sWarning
            aPoints.append(sDesc)

            #Détermination des périodes d'activités
            ### 'period': [False, False, True, True, True, True, True, False, False, False, False, False],
            ### aPoints.append("***Period (Janvier->Decembre) " + str(aFeat["properties"].get("period","")))
            bActive:bool=False
            lMonth:int=0
            lActiveStart:int=0
            lActiveStop:int=0
            oTimes:list = {}
            for month in aFeat["properties"]["period"]:
                lMonth += 1
                ### aPoints.append("***  Month " + str(month))
                if (not bActive) and month:
                    lActiveStart = lMonth
                    bActive = True
                if bActive and ((not month) or lMonth==12) :
                    if lMonth==12:
                        lActiveStop = lMonth
                    else:
                        lActiveStop = lMonth-1
                    sPeriod:str = "UTC(01/{0:0=2d}->31/{1:0=2d})".format(lActiveStart, lActiveStop)
                    oTimes.update({str(len(oTimes)+1): [sPeriod, "ANY(00:00->23:59)"]})
                    ### aPoints.append("***  --> Period" + str(oTimes))
                    bActive = False

            sActiv:str = "*AActiv [TIMSH] Survol interdit"
            if aFeat["properties"]["elevation"]:
                sActiv += " à moins de " + sAlt + " - Période d'activation: "
            for key,val in oTimes.items():
                sActiv += key + "=" + val[0][3:] + " "
            aPoints.append(sActiv)

            ### aPoints.append('*ATimes {"1": ["UTC(01/01->31/12)", "ANY(00:00->23:59)"]}')
            aPoints.append('*ATimes ' + str(oTimes).replace("'",'"'))
            aPoints.append("AH " + sFeet + "FT AGL")
            aPoints.append("AL SFC")

            return True

        # Début de traitement
        aKmlPolygon:list = None
        aPoints:list = []
        if sFile:
            oKml = bpaTools.readJsonFile(sPath + sFile)
            lFeatNumber:int = 0
            for aFeat in oKml["features"]:
                lFeatNumber += 1
                lSubFeatNumber:int = 0
                #makeOpenairHead()
                #aKmlPolygon = aFeat["geometry"]["coordinates"][0]
                #if not (isinstance(aKmlPolygon[0][0], float)):
                #    aKmlPolygon = aKmlPolygon[0]
                #coord2Openair(aKmlPolygon)
                #aPoints.append("")
                aKmlPolygon = aFeat["geometry"]["coordinates"]
                if (isinstance(aKmlPolygon[0][0][0], float)):
                    if makeOpenairHead(aFeat)==True:
                        coord2Openair(aKmlPolygon[0])
                        aPoints.append("")
                elif(isinstance(aKmlPolygon[0][0][0], list)):
                    for aSubFeat in aKmlPolygon:
                        lSubFeatNumber += 1
                        if makeOpenairHead(aFeat)==True:
                            coord2Openair(aSubFeat[0])
                            aPoints.append("")
        else:
            #use this bloc with convert kml content --> <coordinates>6.83116684293515,45.1887962663991 6.83122924345731,45.18753 ...
            aKmlPolygon = [[6.83116684293515,45.1887962663991],[6.83122924345731,45.1875332872193],[6.83131352292729,45.1869840167388],[6.83071009330213,45.1864871164329],[6.83053717594824,45.185745380592],[6.82986247584278,45.1853947065231],[6.82922047700472,45.1849278799351],[6.82886365843867,45.1838761316866],[6.82823613193378,45.1830008963238],[6.82738597032615,45.1824890057639],[6.82666879567534,45.1821110152744],[6.82591106478646,45.1817344113565],[6.82539673823843,45.1813494568795],[6.82497534886682,45.1811338530004],[6.82403054464708,45.1809937028924],[6.82167915632423,45.1808972808342],[6.82089792813593,45.1811401743407],[6.82015128427647,45.1807527705459],[6.81934193996408,45.1808092377071],[6.81751060505921,45.1807856490084],[6.81637477118819,45.1808245096688],[6.81555561350889,45.1807375032247],[6.81469981545173,45.1807092563641],[6.81384009663329,45.1806236243942],[6.81305955083956,45.1805065236058],[6.81195056611447,45.1803431277669],[6.81155863058669,45.1805578128995],[6.81217358554118,45.1812269518724],[6.81274406825428,45.1818400953196],[6.81339373640988,45.1824217734848],[6.81413728826758,45.1833971857846],[6.81410678564142,45.1845253672372],[6.81363626247196,45.1853753849769],[6.8137723066816,45.1861759122728],[6.81401106724276,45.187289248416],[6.81481792630372,45.1887812957156],[6.81673844619317,45.1902065883934],[6.81637589671788,45.1908516302397],[6.8163686858995,45.191340735987],[6.81638895016227,45.1922314920441],[6.81658461008764,45.1927136593541],[6.81731559390163,45.1932925405767],[6.81829986044738,45.1940065335207],[6.82060093655784,45.1955381375083],[6.8210990556066,45.1968726393021],[6.82179615753086,45.1981428127009],[6.8220253009274,45.1991126883914],[6.82225445228593,45.2000825638198],[6.82243516775035,45.2009390718592],[6.82379987264115,45.2012661577135],[6.82493808449342,45.2012559105484],[6.82619606839583,45.2012127889121],[6.82768374997701,45.2009604784701],[6.82884678081721,45.2007192863933],[6.82985733243216,45.2006270982441],[6.83084109295987,45.2007371176208],[6.83170114758968,45.2008226190614],[6.83245836340438,45.2005953211373],[6.83266751462437,45.1994953815465],[6.83264698799016,45.1986046270297],[6.83245116869721,45.1981224872431],[6.83217616892014,45.197671823096],[6.83211391273564,45.1973576368303],[6.83302435073977,45.1975851799175],[6.83277218586644,45.1968749221773],[6.83220330038046,45.1962905680771],[6.8320094637158,45.1958371168124],[6.83201456742522,45.1953193205273],[6.83135470366751,45.1945943037634],[6.83121247624648,45.1937077292448],[6.83125225068899,45.1931024730144],[6.83093985492477,45.1921067144735],[6.8308709061197,45.1911025978779],[6.83094534475593,45.1904098820422],[6.83127503175966,45.1898809421748],[6.83148102830672,45.1893274919413],[6.83116684293515,45.1887962663991]]
            coord2Openair()

        if sFile:
            sFileDst = sFile.replace(".geojson", ".txt")
            bpaTools.writeTextFile(sPath + sFileDst, "\n".join(aPoints))
            print("\nFile created -> " + sPath + sFileDst)
        else:
            print("--Deb--")
            print("\n".join(aPoints))
            print("--Fin--")
        return



if __name__ == '__main__':
    o = GeoBiodivSports()
    #                        OLD = "2017","2018","2019","2020","2021","2022","2023","2024","2025"
    o.geoJsonBiodivSports2Openair(["2022","2023","2024","2025"],
                                "D:/_Users_/BPascal/_4_Src/GitHub/poaff/input/LPO_Biodiv/Biodiv-sports-api/",
                                "20240101_biodiv-sports-fr_janv.geojson")

###     Procédure de récupération des Parcs & ZSMs
###     a/ Utiliser l'API pour récupérer l'ensemble des tracés de type "Aérien"
###         Lien - https://biodiv-sports.fr/api/v2/sensitivearea/?format=geojson&page_size=10000&language=fr&practices=3
###     b/ Enregistrer le fichier sous cette forme:
###         Dossier - D:\_Users_\BPascal\_4_Src\GitHub\poaff\input\LPO\Biodiv-sports-api
###     	Nommage - AAAAMMJJ_biodiv-sports-fr.geojson
###     c/ Ouvrir Spyder ; l'éditeur Python
###     d/ Ouvrir le projet : 'geoRef' puis éditer le source 'geoBiodiv2Openair.py'
###     e/ Modifier les paramètres depuis l'appel de la fonction 'geoJsonBiodivSports2Openair('
###     	Dates de mises aà jour acceptables pour les ZSMs 	--> ["2022","2023"]
###     	Dossier d'accès au fichier geojson					--> "D:/_Users_/BPascal/_4_Src/GitHub/poaff/input/LPO/Biodiv-sports-api/"
###     	Fichier geojson extrait du site Biodiv-sports		--> "20230401_biodiv-sports-fr.geojson"
###     f/ Les fichiers de type Openair sont automatiquement créés :
###     	Exemple:
###     		File source - 20230401_biodiv-sports-fr.geojson
###     		File dest 1 - 20230401_biodiv-sports-fr_Parc.txt
###     		File dest 2 - 20230401_biodiv-sports-fr_Zsm-Active.txt
###             File dest 3 - 20230401_biodiv-sports-fr_Zsm-OLD.txt
###         	File dest 4 - Optionnel avec warning (voir action suivante) - [20230401_biodiv-sports-frZsm_Others.txt]
###     g/ Warning - en présence d'un fichier [AAAAMMJJ_biodiv-sports-frZsm_Others.txt]
###     	Il faut absoluement analyser le contenu et revoir et/ou compléter les filtrages 'bZSM' ou 'bParc' qui sont réalisés dans la fonction 'geoJsonBiodivSports2Openair'
