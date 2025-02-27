class Deobfuscator(ast.NodeTransformer):
    def __init__(self, mapping):
        self.mapping = {v: k for k, v in mapping.items()}

    def visit_Name(self, node):
        if node.id in self.mapping:
            node.id = self.mapping[node.id]
        return node

    def visit_FunctionDef(self, node):
        if node.name in self.mapping:
            node.name = self.mapping[node.name]
        self.generic_visit(node)
        return node