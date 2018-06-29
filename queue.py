from collections import deque

class Queue:
    def __init__(self):
        self.entries = deque()
        self.entry_set = set()

    def add(self, entry):
        self.entries.append(entry)
        self.entry_set.add(entry)

    def extend(self, entries):
        for entry in entries:
            self.add(entry)

    def remove(self):
        entry = self.entries.popleft()
        self.entry_set.remove(entry)
        return entry

    def __contains__(self, key):
        return key in self.entry_set
