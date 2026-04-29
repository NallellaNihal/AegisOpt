import ast

class ProfilerAgent:
    def analyze(self, code):
        tree = ast.parse(code)
        num_functions = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
        num_loops = sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))

        return {
            "functions": num_functions,
            "loops": num_loops
        }