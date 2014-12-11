

import os


gdalCMD1 = 'ogr2ogr -f "ESRI Shapefile" -sql "SELECT * FROM '+j+k+'_erase WHERE GID='+i+'" /Users/danielmsheehan/Desktop/ogr_test/processing/buffer_clip_exp.shp /Users/danielmsheehan/Desktop/ogr_test/point.shp'


#ogr2ogr -f "ESRI shapefile" output.shp input.shp -clipsrc AdminPoly.shp -clipsrclayer AdminPoly -clipsrcsql "SELECT * FROM AdminPoly WHERE AttributeName_in_AdminPoly='Some_value'"


gdalCMD1 = 'ogr2ogr -f "ESRI Shapefile"  /Users/danielmsheehan/Desktop/ogr_test/processing/buffer_clip_exp.shp /Users/danielmsheehan/Desktop/ogr_test/point.shp'

print gdalCMD1
os.system(gdalCMD1)