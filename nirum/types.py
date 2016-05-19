""":mod:`nirum.types`
~~~~~~~~~~~~~~~~~~~~~

"""
import collections

__all__ = 'NameDict',


class NameDict(collections.Mapping):

    def __init__(self, names):
        self.facial_names = dict(names)
        self.behind_names = {b: f for f, b in names}
        assert len(names) == len(self.behind_names) == len(self.facial_names)

    def __getitem__(self, facial_name):
        return self.facial_names[facial_name]

    def __iter__(self):
        return iter(self.facial_names)

    def __len__(self):
        return len(self.facial_names)
