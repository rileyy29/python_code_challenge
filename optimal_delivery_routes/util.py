import osmnx as ox
import networkx as nx
from neighbour import h_distance

def get_osmnx(start, locations):
    max_distance = max(h_distance(start, loc) for loc in locations) * 1000 #in m
    radius = max(5000, int(max_distance + 1000))  

    G = ox.graph_from_point(start, dist=radius, network_type='drive')
    all_points = [start] + locations
    routes = []

    for i in range(len(all_points) - 1):
        try:
            orig_node = ox.distance.nearest_nodes(G, all_points[i][1], all_points[i][0])
            dest_node = ox.distance.nearest_nodes(G, all_points[i + 1][1], all_points[i + 1][0])
            route = nx.shortest_path(G, orig_node, dest_node, weight='length')
            routes.append(route)
        except Exception as e:
            print(f"Error finding route between {all_points[i]} and {all_points[i + 1]}: {e}")

    return G, routes