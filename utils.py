from shapely.geometry import Polygon
from shapely.affinity import rotate

def iou_polygons(a, b):
    ''' Calculates Intersection Over Union (IOU) ofr two polygones a & b.
        a and b should be a list of tuples of vertices [(x1,y1),...,(x22,y22)] 
        like this:
            
        (x11,y11) ************* (x2,y2)
                  *           *
                  *           *
                  *           *
        (x1,y1)   ************* (x22,y22)   
        
    ''' 
    
    a = Polygon(a)
    b = Polygon(b)
    # Polygon of intersection
    pol_i = a.intersection(b)
    pol_u = a.union(b)
   
    area_i = pol_i.area
    area_u = pol_u.area
    iou = float(area_i) / float(area_u + 1e-6)

    return iou
