import fiona
from shapely.geometry import shape
from copy import deepcopy

with fiona.open("planning_neighborhoods.shp", "r") as n: 

    with fiona.open("Schools_Private_Pt.shp", "r") as s:

        # create a schema for the attributes
        outSchema =  deepcopy(s.schema)
        outSchema['properties'].update(n.schema['properties'])

        with fiona.open ("Schools_withNbhd.shp", "w", s.driver, outSchema, s.crs) as output:

            for school in s: 
                for neighborhood in n:
                    # check if point is in polygon and set attribute
                    if shape(school['geometry']).within(shape(neighborhood['geometry'])):  
                        school['properties']['neighborho'] = neighborhood['properties']['neighborho'] 
                    # write out
                        output.write({                                 
                            'properties': school['properties'], 
                            'geometry': school['geometry']
                        })