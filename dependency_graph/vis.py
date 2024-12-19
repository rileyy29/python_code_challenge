import matplotlib.pyplot as plt
import networkx as nx

def print_graph(graph, data):
    pos = nx.spring_layout(graph)  
    plt.figure(figsize=(10, 8))

    nx.draw(graph, pos, with_labels=False, node_color="lightblue", node_size=2000, edge_color="gray")

    labels = {node: f"{node}\n{data[node].get('value', '')}" for node in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=8)

    plt.title("Dependency Graph")
    plt.savefig(".output/dependency_graph.png", format="png")
    plt.close()