"""Intercepting imports to note the time that they occurred for caching script results.

xdp could do this, or scripts could check themselves. Former probably easier because scripts end so have to save files.

On second thoughts: primary dependency analysis tool should be static i.e not need to run the script.
"""
import sys
import importlib.machinery


class ImportRecorder(importlib.machinery.PathFinder):
    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        spec = importlib.machinery.PathFinder.find_spec(fullname, path, target)
        print(spec)
        return spec

sys.meta_path.insert(2, ImportRecorder())

import pandocfilters
import os
import builtins
print('DONE')

import pandocfilters

print('DONE')