"""
absolute vs relative path?

cache nodes on identity or value? comparing value means walking the entire subtree below node. what about case of a single
change to a root file that has lots of outputs among children? in first instance, too bad. but could maybe make a simple diff?

output types:
    html - templates, navigation etc

"""
# https://hackage.haskell.org/package/pandoc-types-1.22/docs/Text-Pandoc-Definition.html
from dataclasses import dataclass, replace
import os
import time
from typing import Tuple
import json
from subprocess import  check_output, run, Popen, PIPE
from functools import lru_cache
from pandocfilters import walk


def file_loader(load, cache={}):
    def lookup(path):
        try:
            record = cache[path]
        except KeyError:
            pass
        else:
            if os.path.getmtime(path) < record[0]:
                return record[1]
        result = load(path)
        cache[path] = time.time(), result
        return result
    return lookup


@file_loader
def load(path) -> dict:
    ast = json.loads(check_output(['pandoc', path, '-t', 'json']))
    return dict(t='File', c=[ast['meta'], ast['blocks']])

def include(key, value, format, meta):
    if key == 'Code' and 'include' in value[0][1]:
        return load(value[1])

def save(obj):
    if key == 'Header' and
    p = Popen(['pandoc', '-f', 'json', '-o', path], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout_data, stderr_data = p.communicate(json.dumps(obj).encode())

@dataclass(frozen=True)
class Node:
    ...

@dataclass(frozen=True)
class Pandoc(Node):
    typ: str
    contents:

@dataclass(frozen=True)
class INode(Node):
    children: Tuple[Node]


def from_pandoc_ast(obj):
    if isinstance(obj, dict):
        if 't' in obj:
            return Pandoc(obj['t'], from_pandoc_ast(['c']))

    if isinstance(obj, list):
        for item in obj:



@dataclass(frozen=True)
class Leaf:
    pass

@dataclass(frozen=True)
class INode(Node):
    children: Tuple[Node,...]

@dataclass(frozen=True)
class File(INode):
    path: str
    meta: dict

@dataclass(frozen=True)
class Include(Leaf):
    path: str


def include(node):
    if isinstance(node, Include):
        node = include(load(node.path))
    elif isinstance(node, INode):
        children = tuple(include(child) for child in node.children)
        if children != node.children:
            node = replace(node, children=children)
    return node



def make_funkbungler

def make_output(node):
    for node in node.walk:
        if is_output(node):
            if not node.is_done:
                # TODO Make file.
                node.is_done = True

def get_labels(node):
    for node in node.walk:
        if is_label(node):
            # add to context
        elif is_context(node):
            # add to context

def get_outputs():
    for node in node.walk:
        if node.

def resolve_references(node):
    for node in node.walk:
        if is_reference()

get_outputs(get_labels(include(load('root.md'))))


# Unless we know that no files have changed, we can't cache include.
# def include(node):
#     # Recursively load all includes. If node is not a leaf and has no load dependencies, then result is cached.
#     if isinstance(node, Leaf):
#         if is_include(node):
#             return include(load(node.filename))
#         else:
#             return node
#     elif isinstance(node, NotLeaf):
#         try:
#             return node.cache['include']
#         except KeyError:
#             pass
#         children = tuple(include(child) for child in node.children)
#         if children != node.children:
#             result = replace(node, children=children)
#
#         node.cache['include'] = result
#     else:
#         raise ValueError('Unknown node.')



def map_traversal(f, root):
    """Replace all root and its descendants by result of f.

    If unchanged, returns input argument.
    """
#    for



class Filter(Node):


"""For efficiency we want equality based on identity. Since Nodes """
@dataclass(frozen=True, eq=False)
class Node:
    ...

class Load(Node):
    filename: str
    loaded: Node # not recursive

class Include(Node):
    input: Node

    ...

ast = Include(Load(filename))


def load_includes(node):
    """Cannot implement recursively as we are caching calls."""
    if isinstance(node, 'Include'):


    # Include nodes have no children, so can go through leaves of node.
    for node in root.leaves:
        if node.type == 'include':

        # No children?
        return load_includes(node(node.file, node.format, node.options))
    else:
        node = replace(node, children=load_includes())
