class Stack:
    def __init__(self):
        self.entries = []
        self.entry_set = set()

    def add(self, entry):
        self.entries.append(entry)
        self.entry_set.add(entry)

    def extend(self, new_entries):
        new_entries = new_entries[::-1]
        for entry in new_entries:
            self.add(entry)

    def remove(self):
        entry = self.entries.pop()
        self.entry_set.remove(entry)
        return entry

    def __contains__(self, key):
        return key in self.entry_set
