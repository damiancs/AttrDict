"""
attrdict contains several mapping objects that allow access to their
keys as attributes.
"""
from attrdict.default import AttrDefault
from attrdict.dictionary import AttrDict
from attrdict.mapping import AttrMap

__all__ = ['AttrMap', 'AttrDict', 'AttrDefault']
