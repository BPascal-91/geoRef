#!/usr/bin/env python3



try:
    import bpaTools
except ImportError:
    ### Include local modules/librairies  ##
    import os
    import sys
    module_dir = os.path.dirname(__file__)
    aixmParserLocalSrc  = "../../aixmParser/src/"
    sys.path.append(os.path.join(module_dir, aixmParserLocalSrc))
    import bpaTools

from frenchConfig import *

###  Context applicatif  ####
appName                 = bpaTools.getFileName(__file__)
appPath                 = bpaTools.getFilePath(__file__)
appVersion              = bpaTools.getVersionFile()
appId                   = appName + " v" + appVersion
inpPath                 = appPath + "../input/"
outPath                 = appPath + "../output/"
logFile                 = outPath + "_" + appName + ".log"


def createGeoJsonFile(sFileSrc, sCountryName, sCountryCode, sCountryIsoCode, sCountryDepCode, oArea, iIdx=-1) -> None:
    if iIdx==-1:
        sName = sCountryName
    elif iIdx>-1 and sCountryName=="France":
        sName = oFranceNames.get(str(iIdx), str(iIdx))
    else:
        sName = str(iIdx)

    #Property for new GeoJSON
    oProperties = {"name":sName}
    if iIdx>-1:
        oProperties.update({"id":str(iIdx)})
    oProperties.update({"countryName": sCountryName})
    oProperties.update({"countryCode": sCountryCode})
    oProperties.update({"countryIsoCode": sCountryIsoCode})
    if sCountryDepCode!=sCountryCode:
        oProperties.update({"countryDepCode": sCountryDepCode})
    oProperties.update({"src":sFileSrc})
    oProperties.update({"creationDatetime":str(bpaTools.getNowISO())})

    #Feature content
    if iIdx==-1:
        #old = {"type":"FeatureCollection", "features":[oCountry]}
        oNewFeature = {"type":"Feature", "properties":oProperties, "geometry":oArea["geometry"]}
    else:
        oNewFeature = {"type":"Feature", "properties":oProperties, "geometry":{"type":"Polygon", "coordinates":oArea}}
    oMainFeature = {"type":"FeatureCollection", "features":[oNewFeature]}

    #Folder destination
    sDestPath = outPath + sCountryDepCode + "-" + sCountryName + "/"
    bpaTools.createFolder(sDestPath)

    #File destination
    if iIdx==-1:
        sFileDst = "_" + sCountryDepCode + "-" + sCountryName + "-border_allAreas.geojson"
    else:
        sFileDst = sCountryDepCode + "-" + sCountryName + "-border_" + sName + ".geojson"
    bpaTools.writeJsonFile(sDestPath + sFileDst, oMainFeature)

    if iIdx==-1:
        if oArea["geometry"]["type"]=="MultiPolygon":
            iIdx=0
            for oArea in oArea["geometry"]["coordinates"]:
                createGeoJsonFile(sFileSrc, sCountryName, sCountryCode, sCountryIsoCode, sCountryDepCode, oArea, iIdx)
                iIdx+=1
    return


if __name__ == '__main__':
    oLog = bpaTools.Logger(appId, logFile)
    oLog.resetFile()           #Clean du log si demandé

    sPathSrc = inpPath + "borders/ec.europa.eu/"
    #sFileSrc = "CNTR_RG_60M_2020_4326.geojson"       #Small resolution map
    sFileSrc = "CNTR_RG_01M_2020_4326.geojson"       #Hight resolution map
    oLog.info("Loading file: " + sFileSrc, outConsole=True)

    oSrcJson:dict = bpaTools.readJsonFile(sPathSrc + sFileSrc)
    oFeatures = oSrcJson["features"]
    for oCountry in oFeatures:
        sCountryName    = oCountry["properties"]["NAME_ENGL"]
        sCountryName = str(sCountryName).replace(" ","-")
        sCountryCode    = oCountry["properties"]["CNTR_ID"]
        sCountryIsoCode = oCountry["properties"]["ISO3_CODE"]
        oLog.info("Country: ({0}) {1} - {2}".format(sCountryIsoCode, sCountryCode, sCountryName) , outConsole=False)
        #oLog.info("Country: ({0}) {1}".format(sCountryIsoCode, sCountryCode) , outConsole=False)

        if sCountryIsoCode in ["FRA","BLM","PYF","SPM","NCL","WLF","XO","HTI","ATF","GBR","IRL","GGY","JEY","NLD","AND","ITA","CHE","DEU","LIE","BEL","LUX","ESP","PRT","DNK","SVN","SVK","AUT","CZE","HRV","HUN","POL"]:
            # Dependense Code - Codification du pays représantant
            if   sCountryIsoCode in ["BLM","NCL","HTI","WLF","PYF","SPM","ATF","XO"]:       sCountryDepCode="FR"
            elif sCountryIsoCode in ["GGY","JEY"]:                                          sCountryDepCode="UK"
            else:                                                                           sCountryDepCode=sCountryCode

            #Extraction des frontières
            createGeoJsonFile(sFileSrc, sCountryName, sCountryCode, sCountryIsoCode, sCountryDepCode, oCountry)

    print()
    oLog.Report()
    oLog.closeFile()

