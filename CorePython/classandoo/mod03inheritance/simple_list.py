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


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super(IntList, self).__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("IntList only supports integer values.")

    def add(self, item):
        self._validate(item)
        super(IntList, self).add(item)


#> from classandoo.mod03inheritance.simple_list import *
#> sl = SortedList([4, 3, 78, 1])
#> sl.len()
#> sl.add(10)

#> isinstance(3, int)
#> isinstance('hello!', str)
#> isinstance(4.567, bytes) # false
#> sl = SortedList([4, 3, 78, 1])
#> isinstance(sl, SortedList)
#> isinstance(sl, SimpleList)
#> x = []
#> isinstance(x, (float, dict, list))

#> from classandoo.mod03inheritance.simple_list import *
#> il = IntList([1, 2, 3, 4])
#> il.add(19)
#> issubclass(IntList, SimpleList)
#> issubclass(SortedList, SimpleList)