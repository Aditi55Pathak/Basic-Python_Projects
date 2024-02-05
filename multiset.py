class Multiset(object):
    def __init__(self):
        self.item = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.item.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.item:
            self.item.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.item:
            return True
        else:
            return False

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.item)


o = Multiset()
o.add(56)
o.add(7)
