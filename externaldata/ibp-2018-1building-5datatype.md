# Open Smart Home Data Set
Mads Holten Rasmussen, Peter Bonsma, Pieter Pauwels, Jyrki Oraskari, Georg Ferdinand Schneider

## Citation
Please refer to publications and the DOI [![DOI](https://zenodo.org/badge/120334357.svg)](https://zenodo.org/badge/latestdoi/120334357) registered for this repository when using the data in your research.

## Contributing
Please feel free to fork and contribute to the data set in compliance with the issued license. The intention is to have it as a playground use case for manifold data on the web approaches to smart home data.

## The Data

The data set comprises static and dynamic building data.

Filename | Description
--- | ---
MeasurementTurtle | RDF dump of the measurements made using a real world smart home system as RDF dumps in ttl format
00_OpenSmartHomeData.ttl | Meta data describing the observations made by the smart home system measurements
01_LinkOsh.ttl | Links linking instances from 00_OpenSmartHomeData.ttl and 02_BotFromRevit.ttl
02_GeoFromRevit.ttl | BOT export from Revit file (05_Flat.rvt)
02_PropsFromRevit.ttl | PROPS export from Revit file (05_Flat.rvt)
02_GeoFromRevit.ttl | 2D space boundaries from Revit file (05_Flat.rvt)
03_GEOM.ttl | GEOM export generated from the IFC file (04_Flat.ifc)
04_Flat.ifc | IFC model of the flat exported from Revit
05_Flat.rvt | Model of the flat in Revit

https://github.com/TechnicalBuildingSystems/OpenSmartHomeData