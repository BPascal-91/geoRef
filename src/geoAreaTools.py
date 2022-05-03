#!/usr/bin/env python3
from shapely.geometry import Polygon

try:
    import bpaTools
except ImportError:
    ### Include local modules/librairies  ##
    import os
    import sys
    aixmParserLocalSrc  = "../../aixmParser/src/"
    module_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(module_dir, aixmParserLocalSrc))
    import bpaTools

class GeoAreaTools:

    def __init__(self)-> None:
        self.appPath = bpaTools.getFilePath(__file__)
        self.inputPath = self.appPath + "../input/_geoRef/"

    #Extrait d'un KML
    #    <Placemark>
    #   	<name>Coeur simplifié</name>
    #   	<styleUrl>#msn_ylw-pushpin</styleUrl>
    #   	<Polygon>
    #   		<tessellate>1</tessellate>
    #   		<outerBoundaryIs>
    #   			<LinearRing>
    #   				<coordinates>
    #   						4.567594081037547,47.78079200340834,1000 4.5861166155308,47.78137220095762,1000 4.609791016139669,47.77145182942082,1000 4.589300784271398,47.75079834378276,1000 4.604385458324625,47.73948713636213,1000 4.63855473175558,47.7386137227859,1000 4.635674132304429,47.75553973506526,1000 4.661672992880264,47.7627681244672,1000 4.680737409165534,47.75650061640716,1000 4.668407291216978,47.74366573537986,1000 4.662517066118928,47.73542848262965,1000 4.699315700172213,47.73941224869148,1000 4.709481966572547,47.72399534095989,1000 4.716270561505461,47.72175410757549,1000 4.724462774614202,47.72788702065485,1000 4.699655420829798,47.75039012125572,1000 4.705921181336919,47.75347613530635,1000 4.731328410481348,47.74593153501265,1000 4.754464072130793,47.74733139963652,1000 4.780193287212335,47.76674116077788,1000 4.805289980139504,47.75609344918714,1000 4.773770255305132,47.70504345249638,1000 4.797130374623569,47.69055780298787,1000 4.819105095131673,47.68327007116124,1000 4.838482273829832,47.68877937317846,1000 4.837804495044455,47.70402210559008,1000 4.869309613182596,47.69503703265037,1000 4.871223040824646,47.69788093684635,1000 4.870122941596772,47.70557761421091,1000 4.859678395326911,47.71112020980554,1000 4.825521474260608,47.71871079373955,1000 4.829518371197368,47.74363040459704,1000 4.863084597993074,47.75500235335525,1000 4.841490902324591,47.79089186075627,1000 4.867449887860036,47.81590253742435,1000 4.864106884245805,47.82437801614164,1000 4.839769114471118,47.85193246812926,1000 4.851742620864467,47.86267650936727,1000 4.834768859658993,47.86871911807523,1000 4.826536526607884,47.86230488147956,1000 4.805506789763438,47.884037108752,1000 4.810446043178589,47.89135146252685,1000 4.856502228023567,47.87060189513645,1000 4.863866773407752,47.83921196055569,1000 4.894978807343584,47.79922223485448,1000 4.909562800542755,47.80480901060987,1000 4.908041363687355,47.8594205921458,1000 4.963216625004354,47.84795815175949,1000 4.982547862381946,47.85194503888821,1000 4.998477425685175,47.86254631136023,1000 5.013013440691008,47.85035423520062,1000 5.028101389312472,47.84717058429691,1000 5.063800074989235,47.8576456578608,1000 5.090253880136966,47.83741722183107,1000 5.082572164690607,47.82266749646954,1000 5.094273087426271,47.80478973278413,1000 5.054875623420068,47.80411185638126,1000 5.05241762733082,47.83059617375293,1000 5.007004304562955,47.8416335613941,1000 4.988105187096377,47.80271359295712,1000 4.984722395497638,47.76789637875982,1000 5.046682241926677,47.73819839598001,1000 5.058260187937337,47.74296320488147,1000 5.061997446414106,47.7221858335905,1000 5.046842443476123,47.709872591609,1000 5.053932174615707,47.7050048454881,1000 5.09722579024436,47.70265547464918,1000 5.102010689723217,47.71444897200484,1000 5.110282120074226,47.72489098315752,1000 5.128688863289852,47.70951186910484,1000 5.139975053035746,47.70940691775316,1000 5.171441825477028,47.73130313890737,1000 5.186882105403303,47.75986923277007,1000 5.196233332437339,47.79073990853621,1000 5.195930259363681,47.83557146893893,1000 5.160131227296121,47.86940031893249,1000 5.142510061150349,47.86470339753728,1000 5.126807679231405,47.81559442970795,1000 5.116548442979174,47.81560401493535,1000 5.111532115867899,47.85963310822098,1000 5.09042535853043,47.85613968876984,1000 5.091441687665242,47.86478884695176,1000 5.104614257920952,47.87245912059531,1000 5.103056437203408,47.87452521921718,1000 5.090788948587153,47.88058327130968,1000 5.080139188298154,47.88057561330744,1000 5.051939671218413,47.87328445556581,1000 5.047371701656964,47.87770315272896,1000 5.074639525618309,47.88624302334314,1000 5.080790450195925,47.88948484894482,1000 5.07579872828055,47.89994723234508,1000 5.062509733966445,47.90443769365619,1000 5.057444372987943,47.89379270875501,1000 5.044771852150705,47.91253082760898,1000 5.056713314296159,47.90880733271222,1000 5.06533437497168,47.91016925157041,1000 5.084042264435425,47.92776350199804,1000 5.072503132839385,47.94405517781243,1000 5.087149561938467,47.9667304810935,1000 5.101288254459666,47.95485695982493,1000 5.108716482738769,47.95547455949637,1000 5.101726133576672,47.97689111466788,1000 5.106431932132218,47.9950009709282,1000 5.083277263004941,48.00526631738145,1000 5.05293326700528,47.99986234867607,1000 5.044579759800659,48.00219141369486,1000 5.04986955676054,48.02755997086534,1000 5.031455699628777,48.03974411879518,1000 4.984968282572639,48.04434693698523,1000 4.944275445506278,48.03608238501425,1000 4.923771523909498,48.02028774860189,1000 4.919474210374979,48.00672071406372,1000 4.95923402661488,47.99340797867232,1000 4.969997210088804,47.97210467063293,1000 4.991430230266076,47.95970537154188,1000 5.012437736229365,47.9627315781422,1000 5.007658116399664,47.97190901821923,1000 5.03558632536657,47.96874835071679,1000 5.017459529868471,47.9563931182583,1000 5.011411879322083,47.94293243548144,1000 5.014976887694472,47.93396031875763,1000 4.976808878504202,47.93066590453912,1000 4.94247012080023,47.90191857050659,1000 4.910785009740484,47.92435546341884,1000 4.903981510872004,47.92335070711073,1000 4.897177302201428,47.90607269195328,1000 4.901778430436224,47.8957983945941,1000 4.89599705327046,47.89477969934776,1000 4.894079840907713,47.90050860376108,1000 4.884067499393936,47.90063641648452,1000 4.874823192782616,47.91548922268288,1000 4.869306350533225,47.91772689483948,1000 4.835640867143494,47.92207920043683,1000 4.830896087876448,47.93318172510691,1000 4.830903137395057,47.92761710370662,1000 4.826263886208846,47.92752204131681,1000 4.824527801317659,47.9212625308816,1000 4.82899003494526,47.9128359780896,1000 4.822222201465063,47.91188561418859,1000 4.816588104549195,47.92087599300933,1000 4.807058463406053,47.92478422751241,1000 4.789384459486485,47.92389757707145,1000 4.78324094092539,47.92307980293156,1000 4.78286360459429,47.91866752733888,1000 4.796647149302951,47.90530128274751,1000 4.775698741776546,47.88373475097697,1000 4.756001052013758,47.8804022726122,1000 4.698099616043317,47.84685958385427,1000 4.7341126539835,47.8331568510057,1000 4.810058631400032,47.81340569156874,1000 4.783733711788624,47.79574632470256,1000 4.777617180532021,47.8132813619859,1000 4.729679910297788,47.82022817171573,1000 4.698103628763053,47.81279035090403,1000 4.694517625746542,47.81835312189136,1000 4.702954681600662,47.82347759714272,1000 4.689723344753737,47.83543276577431,1000 4.676140935187398,47.83825470648144,1000 4.675161394799856,47.85549757731857,1000 4.643216192915432,47.84294964499433,1000 4.60947052540202,47.84753462804376,1000 4.585402104563407,47.82298802518199,1000 4.59960186283962,47.795266979339,1000 4.558499278690055,47.80139155155234,1000 4.55197871519051,47.79570724268708,1000 4.567594081037547,47.78079200340834,1000
    #   					</coordinates>
    #   			</LinearRing>
    #   		</outerBoundaryIs>
    #   	</Polygon>
    #   </Placemark>
    #Utilitaire pour construction d'un format Openair sur la base de données KML
    def kml2Openair(self) -> None:
        self.geoJson2Openair1()
        return

    def geoJsonLPO2Openair(self) -> None:
        #Procédure: 	https://biodiv-sports.fr/api/v2/
        #   ouvrir sensitivearea
        #   cliquer GET /api/v2/sensitivearea/
        #   cliquer Parameters --> 'Try it Out'
        #       language = fr
        #       format = geojson
        #   cliquer Execute
        #   cliquer Download
        #   Enregistrer le fichier sous format type 'YYYYMMDD_LPO_All_Parcs-et-ZSMs.geojson'
        sPath:str="D:/_Users_/BPascal/_4_Src/GitHub/poaff/input/ZSMs/"
        sFileSrc:str="20220415_LPO_All_Parcs-et-ZSMs.geojson"
        sYersFilter=["2021","2022"]
        oLPOdata:dict = bpaTools.readJsonFile(sPath + sFileSrc)
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

            bZSM:bool = False
            bZSM = bZSM or sStruct[:3]=="LPO"                           #Ligue Protection Oiseaux
            bZSM = bZSM or sName=="Grand tétras"
            bZSM = bZSM or sName=="Gypaète barbu"
            bZSM = bZSM or sName=="Aigle royal"
            bZSM = bZSM or sName[:11]=="Tétras lyre"                    #Tétras lyre - hiver
            bZSM = bZSM and ((3 in aPractices) or (7 in aPractices))
            #if bZSM and sUpdtDT[:4] in sYersFilter:
            #    aNewFeatActZsm.append(aFeat)
            #elif bZSM:
            #    aNewFeatNotActZsm.append(aFeat)
            if bZSM:
                aNewFeatActZsm.append(aFeat)

            if not bZSM:
                bParc:bool = False
                bParc = bParc or sStruct[:2]=="PN"                  #Parc National
                bParc = bParc or sStruct[:3]=="PNR"                 #Parc National Régional
                bParc = bParc or sStruct[:3]=="RNF"                 #Réserve Naturelle Nationale
                bParc = bParc or sStruct[:6]=="Asters"              #Réserve Naturelle Nationale
                if bParc:
                    aNewFeatParc.append(aFeat)

            if (not bParc) and (not bZSM):
                aNewFeatOthers.append(aFeat)

        if len(aNewFeatActZsm)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatActZsm})
            sFileDst = sFileSrc.replace("All_Parcs-et-ZSMs","Poaff-Zsm-Active")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson)
            self.geoJson2Openair1(sPath, sFileDst)

        if len(aNewFeatNotActZsm)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatNotActZsm})
            sFileDst = sFileSrc.replace("All_Parcs-et-ZSMs","Poaff-Zsm-NotActive")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson)
            self.geoJson2Openair1(sPath, sFileDst)

        if len(aNewFeatParc)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatParc})
            sFileDst = sFileSrc.replace("All_Parcs-et-ZSMs","Poaff-Parc")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson)
            self.geoJson2Openair1(sPath, sFileDst)

        if len(aNewFeatOthers)>0:
            oNewGeojson:dict  = {"type":"FeatureCollection"}
            oNewGeojson.update({"features":aNewFeatOthers})
            sFileDst = sFileSrc.replace("All_Parcs-et-ZSMs","Poaff-Others")
            bpaTools.writeJsonFile(sPath + sFileDst, oNewGeojson)
            self.geoJson2Openair1(sPath, sFileDst)
        return

    def geoJson2Openair1(self, sPath:str="", sFile:str="") -> None:
        def coord2Openair(aPol:list) -> None:
            for oPoint in aPol:
                oDmsPoint = bpaTools.GeoCoordinates.geoStr2coords(oPoint[1], oPoint[0], "dms", ":", "")    #For native coords with decimals values
                #oDmsPoint = bpaTools.GeoCoordinates.geoStr2coords(oPoint[1], oPoint[0], "dms", ":", "", digit=0)    #For Control with 'Friend Air Tools' - https://mids.be/fat/
                sPoint = "DP " + " ".join(oDmsPoint)
                aPoints.append(sPoint)

        def makeOpenairHead(aFeat:dict) -> None:
            aPoints.append("AC GP")
            sID:str = "LF"
            sName:str = ""
            if "ID_MNHN" in aFeat["properties"]:
                sID += aFeat["properties"]["ID_MNHN"] + "-" + str(lSubFeatNumber)
                sName += aFeat["properties"].get("NOM_SITE","") + " " + sID
            elif "name" in aFeat["properties"]:
                sID += aFeat["properties"].get("name","") + "-" + str(lSubFeatNumber)
                sName += aFeat["properties"].get("name","") + " " + sID
            else:
                sID += "Autoload-" + str(lFeatNumber) + "." + str(lSubFeatNumber)
                sName += "Autoload " + sID
            aPoints.append("AN PROTECT " + aFeat["properties"].get("NOM_SITE","") + " " + sID + " (???m/sol) (FAUNA)")
            aPoints.append("*AUID GUId=! UId=! Id=" + sID)
            if "URL_FICHE" in aFeat["properties"]:
                aPoints.append("*ADescr (c) Pascal Bazile 04/2022 - " + aFeat["properties"].get("OPERATEUR","") + " - " + aFeat["properties"].get("GEST_SITE","") + " - " + aFeat["properties"].get("ID_MNHN","") + " - " + aFeat["properties"]["URL_FICHE"])
                aPoints.append("*AActiv [H24] Survol interdit à moins de ??? mètres sol - (Décret)")
                aPoints.append('*ATimes {"1": ["UTC(01/01->31/12)", "ANY(00:00->23:59)"]}')
            else:
                aPoints.append("*Properties: " + str(aFeat["properties"]))
            aPoints.append("AH 69FT")
            aPoints.append("AL SFC")

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
                    makeOpenairHead(aFeat)
                    coord2Openair(aKmlPolygon[0])
                    aPoints.append("")
                elif(isinstance(aKmlPolygon[0][0][0], list)):
                    for aSubFeat in aKmlPolygon:
                        lSubFeatNumber += 1
                        makeOpenairHead(aFeat)
                        coord2Openair(aSubFeat[0])
                        aPoints.append("")

        else:
            #use this bloc with convert kml content --> <coordinates>6.83116684293515,45.1887962663991 6.83122924345731,45.18753 ...
            aKmlPolygon = [[6.83116684293515,45.1887962663991],[6.83122924345731,45.1875332872193],[6.83131352292729,45.1869840167388],[6.83071009330213,45.1864871164329],[6.83053717594824,45.185745380592],[6.82986247584278,45.1853947065231],[6.82922047700472,45.1849278799351],[6.82886365843867,45.1838761316866],[6.82823613193378,45.1830008963238],[6.82738597032615,45.1824890057639],[6.82666879567534,45.1821110152744],[6.82591106478646,45.1817344113565],[6.82539673823843,45.1813494568795],[6.82497534886682,45.1811338530004],[6.82403054464708,45.1809937028924],[6.82167915632423,45.1808972808342],[6.82089792813593,45.1811401743407],[6.82015128427647,45.1807527705459],[6.81934193996408,45.1808092377071],[6.81751060505921,45.1807856490084],[6.81637477118819,45.1808245096688],[6.81555561350889,45.1807375032247],[6.81469981545173,45.1807092563641],[6.81384009663329,45.1806236243942],[6.81305955083956,45.1805065236058],[6.81195056611447,45.1803431277669],[6.81155863058669,45.1805578128995],[6.81217358554118,45.1812269518724],[6.81274406825428,45.1818400953196],[6.81339373640988,45.1824217734848],[6.81413728826758,45.1833971857846],[6.81410678564142,45.1845253672372],[6.81363626247196,45.1853753849769],[6.8137723066816,45.1861759122728],[6.81401106724276,45.187289248416],[6.81481792630372,45.1887812957156],[6.81673844619317,45.1902065883934],[6.81637589671788,45.1908516302397],[6.8163686858995,45.191340735987],[6.81638895016227,45.1922314920441],[6.81658461008764,45.1927136593541],[6.81731559390163,45.1932925405767],[6.81829986044738,45.1940065335207],[6.82060093655784,45.1955381375083],[6.8210990556066,45.1968726393021],[6.82179615753086,45.1981428127009],[6.8220253009274,45.1991126883914],[6.82225445228593,45.2000825638198],[6.82243516775035,45.2009390718592],[6.82379987264115,45.2012661577135],[6.82493808449342,45.2012559105484],[6.82619606839583,45.2012127889121],[6.82768374997701,45.2009604784701],[6.82884678081721,45.2007192863933],[6.82985733243216,45.2006270982441],[6.83084109295987,45.2007371176208],[6.83170114758968,45.2008226190614],[6.83245836340438,45.2005953211373],[6.83266751462437,45.1994953815465],[6.83264698799016,45.1986046270297],[6.83245116869721,45.1981224872431],[6.83217616892014,45.197671823096],[6.83211391273564,45.1973576368303],[6.83302435073977,45.1975851799175],[6.83277218586644,45.1968749221773],[6.83220330038046,45.1962905680771],[6.8320094637158,45.1958371168124],[6.83201456742522,45.1953193205273],[6.83135470366751,45.1945943037634],[6.83121247624648,45.1937077292448],[6.83125225068899,45.1931024730144],[6.83093985492477,45.1921067144735],[6.8308709061197,45.1911025978779],[6.83094534475593,45.1904098820422],[6.83127503175966,45.1898809421748],[6.83148102830672,45.1893274919413],[6.83116684293515,45.1887962663991]]
            coord2Openair()

        if sFile:
            sFileDst = sFile.replace(".geojson", ".txt")
            bpaTools.writeTextFile(sPath + sFileDst, "\n".join(aPoints))
        else:
            print("--Deb--")
            print("\n".join(aPoints))
            print("--Fin--")
        return


    #Utilitaire pour construction des zones de référence
    def makeZoneRef(self) -> None:
        oDstList:list = []
        oPoint:dict = {}

        #Format d'entrée: fichier JSON extrait d'une 'Task' - http://xcglobe.com/ways
        sName = "French-Ext"         #French, French-Ext, Corse; LaReunion; Tahiti; GuyaneFr etc ../..
        sFile = self.inputPath + sName + ".json"

        oSrcJson:dict = bpaTools.readJsonFile(sFile)
        for oPoint in oSrcJson["points"]:
            oDstList.append([oPoint["lng"], oPoint["lat"]])
        print("self.a" + sName + " = " + str(oDstList))
        print("/!\ Warning - remplacer le dernier point par la valeur du premier point pour garantir un polygone fermé !")
        return

    #Utilitaire pour convertir un contenu GeoJSON en Openair
    def geoJson2Openair2(self) -> None:
        sFileSrc = self.appPath + "../../poaff/input/_geoRef/geoPWCFrenchAlps_border.geojson"
        sFileDst = self.appPath + "../../poaff/input/_geoRef/geoPWCFrenchAlps_border.txt"
        sOutput:str= ""
        oSrc:dict = bpaTools.readJsonFile(sFileSrc)
        oFeatures = oSrc["features"]
        oFirstFeature = oFeatures[0]
        oCoords = oFirstFeature["geometry"]["coordinates"][0]
        for oPoint in oCoords:
            oDmsPoint = bpaTools.GeoCoordinates.geoStr2coords(oPoint[1], oPoint[0], "dms", ":", " ")
            sOutput += "DP {0}\n".format(" ".join(oDmsPoint))
        bpaTools.writeTextFile(sFileDst, sOutput)
        return

    #Test pour déterminer l'intersection du périmètre géographique de deux zones GeoJSON
    def jsonIntersectionTst(self) -> None:
        ref = Polygon([(2.220612,48.380882),(2.220612,48.654686),(2.861938,48.654686),(2.861938,48.380882),(2.220612,48.380882)])
        zAucuneIntersection = Polygon([(1.874542,48.562068),(2.031097,48.493857),(2.070923,48.412796),(2.068176,48.337082),(1.908875,48.328865),(1.779785,48.467458),(1.874542,48.562068)])
        zIntersection = Polygon([ (2.097015,48.522972),(2.355194,48.482935),(2.384033,48.402768),(2.298889,48.310601),(2.110748,48.373584),(2.097015,48.522972)])
        zInclusion = Polygon([(2.364807,48.545705),(2.569427,48.602041),(2.562561,48.463816),(2.364807,48.545705)])

        sAucuneIntersection1 = self.jsonIntersectionExe(ref, zAucuneIntersection)
        print("sAucuneIntersection1 - " + str(sAucuneIntersection1))
        sIntersection1 = self.jsonIntersectionExe(ref, zIntersection)
        print("sIntersection1 - " + sIntersection1)
        sInclusion1 = self.jsonIntersectionExe(ref, zInclusion)
        print("sInclusion1 - " + sInclusion1)

        """
        sAucuneIntersection1 = self.jsonIntersectionExe(ref, zAucuneIntersection)
        sAucuneIntersection2 = self.jsonIntersectionExe(zAucuneIntersection, ref)
        if sAucuneIntersection1 == sAucuneIntersection2:
            print("sAucuneIntersection1 == sAucuneIntersection2: " + sAucuneIntersection1)

        sIntersection1 = self.jsonIntersectionExe(ref, zIntersection)
        sIntersection2 = self.jsonIntersectionExe(zIntersection, ref)
        if sIntersection1 == sIntersection2:
            print("sIntersection1 == sIntersection2:\n  =/ " + sIntersection1)
        else:
            print("sIntersection1 != sIntersection2:\n  1/ " + sIntersection1 + "\n  2/ " + sIntersection2)

        sInclusion1 = self.jsonIntersectionExe(ref, zInclusion)
        sInclusion2 = self.jsonIntersectionExe(zInclusion, ref)
        if sInclusion1 == sInclusion2:
            print("sInclusion1 == sInclusion2:\n  =/ " + sInclusion1)
        """
        return

    def jsonIntersectionExe(self, ref, zone) -> str:
        sCoods:str = ""

        bDisjoint = ref.disjoint(zone)
        #print("disjoint " + str(bDisjoint))
        if bDisjoint:
            return None

        bContains = ref.contains(zone)
        #print("contains " + str(bContains))
        #bWithin   = ref.within(zone)
        #print("within "   + str(bWithin))

        #oDiff = ref.intersection(zone)
        #print("intersection:   ", oDiff)
        oDiff = ref.difference(zone)
        #print("difference -> ", oDiff)
        #oDiff = ref.exterior.difference(zone.exterior)
        #oDiff = ref.symmetric_difference(zone)
        #print("symmetric_difference:   ", oDiff)

        #Get external area
        if not oDiff.is_empty:
            oList:list = list(oDiff.exterior.coords)
            for p in oList:
                sCoods += "[{0},{1}],".format(p[0],p[1])

            #Get internal area for make the empty area(s)
            if bContains and oDiff.interiors:
                for oArea in oDiff.interiors:
                    for p in oArea.coords:
                        sCoods += "[{0},{1}],".format(p[0],p[1])

            sCoods = sCoods[:-1]
        return sCoods

if __name__ == '__main__':
    o = GeoAreaTools()
    #o.jsonIntersectionTst()
    #o.makeZoneRef()         #Utilitaire pour construction des zones de référence
    #o.kml2Openair()         #Utilitaire pour convertion d'un contenu KML en Openair
    #o.geoJson2Openair1("D:/_Users_/BPascal/_4_Src/Src_Python/git/poaff/input/Parcs/Pyrennees/geoLoc/", "_PNP-CoeurDuParc_hr.geojson")
    #o.geoJson2Openair1("D:/_Users_/BPascal/_4_Src/Src_Python/git/poaff/input/Parcs/Pyrennees/geoLoc/", "_PNP_SurvolVolVoile_hr.geojson")
    #o.geoJson2Openair1("D:/_Users_/BPascal/_4_Src/Src_Python/git/poaff/input/Parcs/Pyrennees/geoLoc/", "_PNP_SurvolVolLibre_hr.geojson")
    #o.geoJson2Openair1("D:/_Users_/BPascal/_4_Src/GitHub/poaff/input/ZSMs/makeOpenair/", "20220409_ZSM_ValdIsere-GorgesDaille.geojson")
    #o.geoJson2Openair2()
    #o.geoJsonLPO2Openair()
    #o.geoJson2Openair1("D:/_Users_/BPascal/_4_Src/GitHub/poaff/input/Parcs/___ZSMs/", "20220423_ZSM-Divers_hr.geojson")
    o.geoJson2Openair1("D:/_Users_/BPascal/_4_Src\GitHub/poaff/input/Parcs/", "20220501_BPa-ZSMs-A-Integrer.geojson")
