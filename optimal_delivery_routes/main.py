from neighbour import get_neighbours
from util import get_osmnx
from vis import print_routes

def gen_map():
    # Example: Preston, UK coordinates
    start_location = (53.759, -2.698) 

    # Test density 
    clustered_locations = [
        (53.760, -2.700), (53.761, -2.699), (53.762, -2.698),
        (53.763, -2.697), (53.764, -2.696), (53.765, -2.695),
        (53.766, -2.694), (53.767, -2.693), (53.768, -2.692),
        (53.769, -2.691), (53.770, -2.690), (53.771, -2.689),
        (53.772, -2.688), (53.773, -2.687), (53.774, -2.686),
        (53.775, -2.685), (53.776, -2.684), (53.777, -2.683),
        (53.778, -2.682), (53.779, -2.681)
    ]
    
    spread_out_locations = [
        (53.800, -2.700), (53.805, -2.715), (53.810, -2.730),
        (53.820, -2.740), (53.830, -2.750), (53.840, -2.760),
        (53.850, -2.770), (53.860, -2.780), (53.870, -2.790),
        (53.865, -3.030), (53.845, -3.020), (53.835, -3.010),
        (53.825, -3.000), (53.815, -2.990), (53.805, -2.980),
        (53.795, -2.970), (53.785, -2.960), (53.775, -2.950),
        (53.765, -2.940), (53.755, -2.930)
    ]

    delivery_locations = clustered_locations + spread_out_locations
    ordered_locations = get_neighbours(start_location, delivery_locations)
    G, routes = get_osmnx(start_location, ordered_locations)
    
    print_routes(G, routes, [start_location] + ordered_locations)
    print("Map with routes saved")

gen_map()