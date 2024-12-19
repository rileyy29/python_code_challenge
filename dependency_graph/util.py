import networkx as nx

from parser import parse_formula

def eval_cell(cell, data, graph, visited):
    if cell in visited:
        raise ValueError("Circular dependency detected")

    visited.add(cell)
    details = data[cell]
    if "value" in details:
        return details["value"]

    formula = details.get("formula")
    if not formula:
        raise ValueError(f"Cell {cell} has no formula or value")

    dependencies = parse_formula(formula)
    local_env = {}
    for dep in dependencies:
        local_env[dep] = eval_cell(dep, data, graph, visited)

    value = eval(formula, {}, local_env)
    data[cell]["value"] = value
    return value

def eval_all(data, graph):
    sorted_cells = list(nx.topological_sort(graph))
    for cell in sorted_cells:
        if "value" not in data[cell]:
            visited = set()
            eval_cell(cell, data, graph, visited)