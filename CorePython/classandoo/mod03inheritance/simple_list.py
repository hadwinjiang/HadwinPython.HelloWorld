class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'


class SortedList(SimpleList):
    def __init__(self, items=()):
        super(SortedList, self).__init__(items)
        self.sort()

    def add(self, item):
        super(SortedList, self).add(item)
        self.sort()


#> from classandoo.mod03inheritance.simple_list import *
#> sl = SortedList([4, 3, 78, 1])
#> sl.len()
#> sl.add(10)