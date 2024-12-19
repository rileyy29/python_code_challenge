import folium

def print_routes(G, routes, all_points):
    m = folium.Map(location=(all_points[0][0], all_points[0][1]), zoom_start=14)

    for i, point in enumerate(all_points):
        folium.Marker(
            location=(point[0], point[1]),
            popup=f"{'Start' if i == 0 else f'Delivery {i}'}",
            icon=folium.Icon(color="green" if i == 0 else "blue")
        ).add_to(m)

    for route in routes:
        route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]
        folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(m)

    m.save(".output/optimal_delivery_routes.html")