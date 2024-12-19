import networkx as nx
import json

from util import eval_all
from vis import print_graph
from graph import build_graph

def main():
    with open('.input/dependency_graph.json', "r") as f:
        data = json.load(f)

    graph = build_graph(data)

    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Cycle detected in the graph")

    eval_all(data, graph)

    print_graph(graph, data)

    for cell, details in data.items():
        print(f"{cell}: {details.get('value')}")

main()
