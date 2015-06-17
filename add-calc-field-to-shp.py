from osgeo import ogr

shapefile = wd+'output/ct2010/ct10.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 1)
layer = dataSource.GetLayer()
new_field = ogr.FieldDefn("Area_TEST", ogr.OFTString)
layer.CreateField(new_field)

for feature in layer:
    geom = feature.GetGeometryRef()
    area = feature.GetField("geoid_text")[-11:]
    feature.SetField("Area_TEST", area)
    layer.SetFeature(feature)

dataSource = None