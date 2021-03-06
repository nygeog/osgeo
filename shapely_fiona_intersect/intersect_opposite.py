import fiona
from shapely.geometry import shape
from copy import deepcopy

with fiona.open("buffer_clip_exp.shp", "r") as n: 

    with fiona.open("point.shp", "r") as s:

        # create a schema for the attributes
        outSchema =  deepcopy(n.schema)
        outSchema['properties'].update(s.schema['properties'])

        with fiona.open ("TEST7.shp", "w", s.driver, outSchema, s.crs) as output:

            for school in s: 
                for neighborhood in n:
                    # check if point is in polygon and set attribute
                    if shape(school['geometry']).within(shape(neighborhood['geometry'])):  
                        #school['properties'] = neighborhood['properties'] 
                    # write out
                        output.write({                                 
                            'properties': neighborhood['properties'], 
                            'geometry': neighborhood['geometry']
                        })