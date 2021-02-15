"""
Credits:
    https://gist.github.com/lrq3000/6175522
    https://github.com/mgedmin/findimports/blob/master/findimports.py
"""
import ast
import importlib
import os
from typing import Any


def get_dependencies(base_filename) -> set:
    """Recursively get dependencies of Python source file."""
    # Record of all visited filenames, which are our dependencies.
    filenames = set()

    class Visitor(ast.NodeVisitor):
        def __init__(self, package: str = None):
            """Construct visitor for a node in the AST of a source file of given package."""
            ast.NodeVisitor.__init__(self)
            self.package = package

        def visit_Import(self, node: ast.Import) -> Any:
            for alias in node.names:
                process_module(alias.name)
            ast.NodeVisitor.generic_visit(self, node)

        def visit_ImportFrom(self, node: ast.ImportFrom) -> Any:
            name = '.' * node.level
            if node.module is not None:
                name += node.module
            full_name = importlib.util.resolve_name(name, self.package)
            process_module(full_name)
            ast.NodeVisitor.generic_visit(self, node)

    def process_module(name):
        try:
            spec = importlib.util.find_spec(name)
        except (ValueError, ModuleNotFoundError):
            return
        if spec is None:
            return
        if spec.origin is None:
            return
        if spec.origin == 'built-in':
            return
        if os.path.splitext(spec.origin)[1] != '.py':
            return
        process_file(spec.origin, name)

    def process_file(filename, package: str = None):
        if filename in filenames:
            return
        filenames.add(filename)
        with open(filename) as file:
            contents = file.read()
        tree = ast.parse(contents)
        visitor = Visitor(package)
        visitor.visit(tree)

    process_file(base_filename)

    return filenames


if __name__ == "__main__":
    filenames = get_dependencies('example.py')
    import sys

    print(sys.prefix)
    print("*** FILENAMES ***")
    for f in filenames:
        print(f)
