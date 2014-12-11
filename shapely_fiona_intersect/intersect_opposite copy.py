import fiona
from shapely.geometry import shape
from copy import deepcopy

import os
#run this only in windows with OSGEO4W Administrator Shell open
import csv

# wi = '/Volumes/Hotel/naas/data/input/'
# wp = '/Volumes/Hotel/naas/data/processing/'

# theCSV = wi+"nyccas/Air_Pollution/NYCCAS_100m_grid/gid_list.csv"

# with open(theCSV, 'rb') as f:
#      reader = csv.reader(f)
#      your_list = list(reader)

# idList = []
# for i in your_list:
#     idList.append(i[2])

# geogList     = ['g']
# radbufListFn = ['r0050m','r0100m','r0250m','r0500m']#,'r1000m']
# radbufListFn = ['r0100m']

# for i in idList:
#     for j in geogList:
#         for k in radbufListFn:
# theBuf = '/Volumes/Hotel/naas/tasks/201411_grid/data/processing/geogs/buffers_exp/'+j+k+'/'+j+k+'_erase_'+i+'.shp'
# thePts = '/Volumes/Hotel/naas/tasks/201411_grid/data/processing/geogs/points/pt_'+i+'.shp'
# theOut = '/Volumes/Hotel/naas/tasks/201411_grid/data/processing/geogs/split_geogs_explode_select/'+j+k+'_ogr/'+j+k+'_erase_'+i+'.shp'

theBuf = 'buffer_clip_exp.shp'
thePts = 'point.shp'
theOut = 'TEST_BBB.shp'

with fiona.open(theBuf, "r") as n: 

    with fiona.open(thePts, "r") as s:

        # create a schema for the attributes
        outSchema =  deepcopy(n.schema)
        outSchema['properties'].update(s.schema['properties'])

        with fiona.open (theOut, "w", s.driver, outSchema, s.crs) as output:

            for school in s: 
                for neighborhood in n:
                    #print i #zz
                    # check if point is in polygon and set attribute
                    if shape(school['geometry']).within(shape(neighborhood['geometry'])):  
                        #school['properties'] = neighborhood['properties'] 
                    # write out
                        output.write({                                 
                            'properties': neighborhood['properties'], 
                            'geometry': neighborhood['geometry']
                        })