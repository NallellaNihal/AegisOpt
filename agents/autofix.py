import ast
import astunparse

class AutoFixAgent:
    def fix(self, code):
        tree = ast.parse(code)

        class Transformer(ast.NodeTransformer):
            def visit_Call(self, node):
                # ❌ Replace eval() with safer alternative
                if isinstance(node.func, ast.Name) and node.func.id == "eval":
                    return ast.Constant(value="SAFE_REMOVED_EVAL")
                return self.generic_visit(node)

        transformer = Transformer()
        new_tree = transformer.visit(tree)

        return astunparse.unparse(new_tree)