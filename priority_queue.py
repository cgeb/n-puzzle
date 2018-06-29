import itertools
from heapq import heappush, heappop

class PriorityQueueElement:
    def __init__(self, priority, count, elem):
        self.priority = priority
        self.count = count
        self.elem = elem
        self.removed = False

    def __lt__(self, other):
        return (self.priority, self.count) < (other.priority, other.count)

class PriorityQueue:
    def __init__(self, *args, **kwargs):
        self.key = kwargs.pop('key', lambda x:x)
        self.entries = []
        self.entry_finder = {}
        self.counter = itertools.count()
        if args:
            for entry in args[0]:
                self.add(entry)

    def __contains__(self, state):
        return state in self.entry_finder

    def __iter__(self):
        return iter(self.entry_finder)

    def add(self, elem):
        count = next(self.counter)
        new_entry = PriorityQueueElement(self.key(elem), count, elem)
        if new_entry.elem in self.entry_finder:
            self.remove_from_finder(new_entry.elem)
        self.entry_finder[elem] = new_entry
        heappush(self.entries, new_entry)

    def extend(self, items):
        for item in items:
            self.add(item)

    def remove_from_finder(self, entry):
        entry = self.entry_finder.pop(entry)
        entry.removed = True

    def remove(self):
        while self.entries:
            entry = heappop(self.entries)
            if not entry.removed:
                del self.entry_finder[entry.elem]
                return entry.elem
