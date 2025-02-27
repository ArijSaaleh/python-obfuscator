import ast
import json
import astunparse
import argparse

class Obfuscator(ast.NodeTransformer):
    def __init__(self):
        self.mapping = {}

    def obfuscate_name(self, name):
        if name not in self.mapping:
            self.mapping[name] = f"var_{len(self.mapping) + 1}"
        return self.mapping[name]

    def visit_Name(self, node):
        node.id = self.obfuscate_name(node.id)
        return node

    def visit_FunctionDef(self, node):
        node.name = self.obfuscate_name(node.name)
        self.generic_visit(node)
        return node

def obfuscate_code(code):
    tree = ast.parse(code)
    obfuscator = Obfuscator()
    obfuscated_tree = obfuscator.visit(tree)
    return obfuscated_tree, obfuscator.mapping

def obfuscated_to_code(obfuscated_tree):
    return astunparse.unparse(obfuscated_tree)

def save_mapping(mapping, filename="mapping.json"):
    with open(filename, "w") as f:
        json.dump(mapping, f)

def load_mapping(filename="mapping.json"):
    with open(filename, "r") as f:
        return json.load(f)

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

def deobfuscate_code(code, mapping):
    tree = ast.parse(code)
    deobfuscator = Deobfuscator(mapping)
    return deobfuscator.visit(tree)

def main():
    parser = argparse.ArgumentParser(description="Obfuscate or Deobfuscate Python code.")
    parser.add_argument('mode', choices=['obfuscate', 'deobfuscate'], help="Mode of operation")
    parser.add_argument('file', help="Python file to process")
    
    args = parser.parse_args()
    
    with open(args.file, 'r') as f:
        code = f.read()

    if args.mode == 'obfuscate':
        obfuscated_tree, mapping = obfuscate_code(code)
        obfuscated_code = obfuscated_to_code(obfuscated_tree)
        save_mapping(mapping)
        print(obfuscated_code)
    elif args.mode == 'deobfuscate':
        mapping = load_mapping()
        deobfuscated_tree = deobfuscate_code(code, mapping)
        deobfuscated_code = obfuscated_to_code(deobfuscated_tree)
        print(deobfuscated_code)

if __name__ == "__main__":
    main()
