import ast

def parse_code(code):
    try:
        tree = ast.parse(code)
        print(ast.dump(tree, indent=4))  # Display the parsed structure of the code
    except SyntaxError as e:
        print(f"Error parsing code: {e}")

class Obfuscator(ast.NodeTransformer):
    def __init__(self):
        self.mapping = {}

    def obfuscate_name(self, name):
        # Simple obfuscation (e.g., replace names with 'var1', 'var2', etc.)
        if name not in self.mapping:
            self.mapping[name] = f"var_{len(self.mapping) + 1}"
        return self.mapping[name]

    def visit_Name(self, node):
        # Obfuscate variable names
        node.id = self.obfuscate_name(node.id)
        return node

    def visit_FunctionDef(self, node):
        # Obfuscate function names
        node.name = self.obfuscate_name(node.name)
        self.generic_visit(node)  # Continue visiting other nodes
        return node

def obfuscate_code(code):
    tree = ast.parse(code)
    obfuscator = Obfuscator()
    obfuscated_tree = obfuscator.visit(tree)
    return obfuscated_tree, obfuscator.mapping

if __name__ == "__main__":
    sample_code = """
def hello_world():
    msg = "Hello, world!"
    print(msg)
hello_world()
"""
    obfuscated_tree, mapping = obfuscate_code(sample_code)
    #print(ast.dump(obfuscated_tree, indent=4))
    print(f"Mapping: {mapping}")
