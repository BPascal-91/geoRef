#!/usr/bin/env python3

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
        appPath = bpaTools.getFilePath(__file__)
        self.inputPath = appPath + "../input/_geoRef/"

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
        aKmlPolygon:list = [[4.567594081037547,47.78079200340834,1000], [4.5861166155308,47.78137220095762,1000], [4.609791016139669,47.77145182942082,1000], [4.589300784271398,47.75079834378276,1000], [4.604385458324625,47.73948713636213,1000], [4.63855473175558,47.7386137227859,1000], [4.635674132304429,47.75553973506526,1000], [4.661672992880264,47.7627681244672,1000], [4.680737409165534,47.75650061640716,1000], [4.668407291216978,47.74366573537986,1000], [4.662517066118928,47.73542848262965,1000], [4.699315700172213,47.73941224869148,1000], [4.709481966572547,47.72399534095989,1000], [4.716270561505461,47.72175410757549,1000], [4.724462774614202,47.72788702065485,1000], [4.699655420829798,47.75039012125572,1000], [4.705921181336919,47.75347613530635,1000], [4.731328410481348,47.74593153501265,1000], [4.754464072130793,47.74733139963652,1000], [4.780193287212335,47.76674116077788,1000], [4.805289980139504,47.75609344918714,1000], [4.773770255305132,47.70504345249638,1000], [4.797130374623569,47.69055780298787,1000], [4.819105095131673,47.68327007116124,1000], [4.838482273829832,47.68877937317846,1000], [4.837804495044455,47.70402210559008,1000], [4.869309613182596,47.69503703265037,1000], [4.871223040824646,47.69788093684635,1000], [4.870122941596772,47.70557761421091,1000], [4.859678395326911,47.71112020980554,1000], [4.825521474260608,47.71871079373955,1000], [4.829518371197368,47.74363040459704,1000], [4.863084597993074,47.75500235335525,1000], [4.841490902324591,47.79089186075627,1000], [4.867449887860036,47.81590253742435,1000], [4.864106884245805,47.82437801614164,1000], [4.839769114471118,47.85193246812926,1000], [4.851742620864467,47.86267650936727,1000], [4.834768859658993,47.86871911807523,1000], [4.826536526607884,47.86230488147956,1000], [4.805506789763438,47.884037108752,1000], [4.810446043178589,47.89135146252685,1000], [4.856502228023567,47.87060189513645,1000], [4.863866773407752,47.83921196055569,1000], [4.894978807343584,47.79922223485448,1000], [4.909562800542755,47.80480901060987,1000], [4.908041363687355,47.8594205921458,1000], [4.963216625004354,47.84795815175949,1000], [4.982547862381946,47.85194503888821,1000], [4.998477425685175,47.86254631136023,1000], [5.013013440691008,47.85035423520062,1000], [5.028101389312472,47.84717058429691,1000], [5.063800074989235,47.8576456578608,1000], [5.090253880136966,47.83741722183107,1000], [5.082572164690607,47.82266749646954,1000], [5.094273087426271,47.80478973278413,1000], [5.054875623420068,47.80411185638126,1000], [5.05241762733082,47.83059617375293,1000], [5.007004304562955,47.8416335613941,1000], [4.988105187096377,47.80271359295712,1000], [4.984722395497638,47.76789637875982,1000], [5.046682241926677,47.73819839598001,1000], [5.058260187937337,47.74296320488147,1000], [5.061997446414106,47.7221858335905,1000], [5.046842443476123,47.709872591609,1000], [5.053932174615707,47.7050048454881,1000], [5.09722579024436,47.70265547464918,1000], [5.102010689723217,47.71444897200484,1000], [5.110282120074226,47.72489098315752,1000], [5.128688863289852,47.70951186910484,1000], [5.139975053035746,47.70940691775316,1000], [5.171441825477028,47.73130313890737,1000], [5.186882105403303,47.75986923277007,1000], [5.196233332437339,47.79073990853621,1000], [5.195930259363681,47.83557146893893,1000], [5.160131227296121,47.86940031893249,1000], [5.142510061150349,47.86470339753728,1000], [5.126807679231405,47.81559442970795,1000], [5.116548442979174,47.81560401493535,1000], [5.111532115867899,47.85963310822098,1000], [5.09042535853043,47.85613968876984,1000], [5.091441687665242,47.86478884695176,1000], [5.104614257920952,47.87245912059531,1000], [5.103056437203408,47.87452521921718,1000], [5.090788948587153,47.88058327130968,1000], [5.080139188298154,47.88057561330744,1000], [5.051939671218413,47.87328445556581,1000], [5.047371701656964,47.87770315272896,1000], [5.074639525618309,47.88624302334314,1000], [5.080790450195925,47.88948484894482,1000], [5.07579872828055,47.89994723234508,1000], [5.062509733966445,47.90443769365619,1000], [5.057444372987943,47.89379270875501,1000], [5.044771852150705,47.91253082760898,1000], [5.056713314296159,47.90880733271222,1000], [5.06533437497168,47.91016925157041,1000], [5.084042264435425,47.92776350199804,1000], [5.072503132839385,47.94405517781243,1000], [5.087149561938467,47.9667304810935,1000], [5.101288254459666,47.95485695982493,1000], [5.108716482738769,47.95547455949637,1000], [5.101726133576672,47.97689111466788,1000], [5.106431932132218,47.9950009709282,1000], [5.083277263004941,48.00526631738145,1000], [5.05293326700528,47.99986234867607,1000], [5.044579759800659,48.00219141369486,1000], [5.04986955676054,48.02755997086534,1000], [5.031455699628777,48.03974411879518,1000], [4.984968282572639,48.04434693698523,1000], [4.944275445506278,48.03608238501425,1000], [4.923771523909498,48.02028774860189,1000], [4.919474210374979,48.00672071406372,1000], [4.95923402661488,47.99340797867232,1000], [4.969997210088804,47.97210467063293,1000], [4.991430230266076,47.95970537154188,1000], [5.012437736229365,47.9627315781422,1000], [5.007658116399664,47.97190901821923,1000], [5.03558632536657,47.96874835071679,1000], [5.017459529868471,47.9563931182583,1000], [5.011411879322083,47.94293243548144,1000], [5.014976887694472,47.93396031875763,1000], [4.976808878504202,47.93066590453912,1000], [4.94247012080023,47.90191857050659,1000], [4.910785009740484,47.92435546341884,1000], [4.903981510872004,47.92335070711073,1000], [4.897177302201428,47.90607269195328,1000], [4.901778430436224,47.8957983945941,1000], [4.89599705327046,47.89477969934776,1000], [4.894079840907713,47.90050860376108,1000], [4.884067499393936,47.90063641648452,1000], [4.874823192782616,47.91548922268288,1000], [4.869306350533225,47.91772689483948,1000], [4.835640867143494,47.92207920043683,1000], [4.830896087876448,47.93318172510691,1000], [4.830903137395057,47.92761710370662,1000], [4.826263886208846,47.92752204131681,1000], [4.824527801317659,47.9212625308816,1000], [4.82899003494526,47.9128359780896,1000], [4.822222201465063,47.91188561418859,1000], [4.816588104549195,47.92087599300933,1000], [4.807058463406053,47.92478422751241,1000], [4.789384459486485,47.92389757707145,1000], [4.78324094092539,47.92307980293156,1000], [4.78286360459429,47.91866752733888,1000], [4.796647149302951,47.90530128274751,1000], [4.775698741776546,47.88373475097697,1000], [4.756001052013758,47.8804022726122,1000], [4.698099616043317,47.84685958385427,1000], [4.7341126539835,47.8331568510057,1000], [4.810058631400032,47.81340569156874,1000], [4.783733711788624,47.79574632470256,1000], [4.777617180532021,47.8132813619859,1000], [4.729679910297788,47.82022817171573,1000], [4.698103628763053,47.81279035090403,1000], [4.694517625746542,47.81835312189136,1000], [4.702954681600662,47.82347759714272,1000], [4.689723344753737,47.83543276577431,1000], [4.676140935187398,47.83825470648144,1000], [4.675161394799856,47.85549757731857,1000], [4.643216192915432,47.84294964499433,1000], [4.60947052540202,47.84753462804376,1000], [4.585402104563407,47.82298802518199,1000], [4.59960186283962,47.795266979339,1000], [4.558499278690055,47.80139155155234,1000], [4.55197871519051,47.79570724268708,1000], [4.567594081037547,47.78079200340834,1000]]
        for oDdPoint in aKmlPolygon:
            oDmsPoint = bpaTools.GeoCoordinates.geoDd2dms(oDdPoint[1],"lat", oDdPoint[0],"lon", ":"," ")
            sPoint = "DP " + " ".join(oDmsPoint)
            print(sPoint)
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


if __name__ == '__main__':
    o = GeoAreaTools()
    #o.makeZoneRef()        #Utilitaire pour construction des zones de référence
    #o.kml2Openair()        #Utilitaire pour récupération d'un contenu KML