def h_distance(coord1, coord2):
    from math import radians, sin, cos, sqrt, atan2
    
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371 

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def get_neighbours(start, locations):
    order = [start]
    current = start
    while locations:
        next_loc = min(locations, key=lambda loc: h_distance(current, loc))
        order.append(next_loc)
        locations.remove(next_loc)
        current = next_loc
    return order