import ast

class FormulaParser(ast.NodeVisitor):
    def __init__(self):
        self.dependencies = []

    def visit_Name(self, node):
        self.dependencies.append(node.id)

    def parse(self, formula):
        tree = ast.parse(formula, mode='eval')
        self.dependencies = []
        self.visit(tree)
        return self.dependencies

def parse_formula(formula):
    try:
        parser = FormulaParser()
        return parser.parse(formula)
    except Exception as e:
        raise ValueError(f"Invalid formula: {formula}")