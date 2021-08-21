def hypervolume(*args):
    print(args)
    print(type(args))


hypervolume(3,4)
# (3, 4)
# <class 'tuple'>


def hypervolume_01(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v


def hypervolume_02(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v