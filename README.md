# osgeo
OSGeo scripts, ogr, ogr2ogr, gdal, etc

gdal/ogr - after installed with qgis, set path
http://gis.stackexchange.com/questions/80954/os-x-mavericks-accessing-gdal-from-terminal-issue
so, in the terminal, use the command:

	export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH

Get formats

	ogrinfo --formats


Install GEOS
http://stackoverflow.com/questions/12578471/oserror-geos-c-could-not-be-found-when-installing-shapely

	brew install geos

