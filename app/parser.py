# parser.py
import ast
import os

def extract_functions(file_path):
    """Extract all functions from a single Python file"""
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno - 1
            end_line = node.end_lineno
            code_chunk = "\n".join(source.splitlines()[start_line:end_line])

            functions.append({
                "name": node.name,
                "code": code_chunk
            })
    return functions

def extract_functions_from_folder(folder_path):
    """Extract all functions from all Python files in a folder"""
    all_functions = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                funcs = extract_functions(file_path)
                for f in funcs:
                    f["file_path"] = file_path  # keep track of origin
                    all_functions.append(f)
    return all_functions
