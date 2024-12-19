import networkx as nx

from parser import parse_formula

def build_graph(data):
    graph = nx.DiGraph()
    for cell, details in data.items():
        formula = details.get("formula")
        if formula:
            dependencies = parse_formula(formula)
            for dep in dependencies:
                graph.add_edge(dep, cell)
        graph.add_node(cell)
    return graph