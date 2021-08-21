
def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


seq = sequence_class(immutable=True)
t = seq("Timbuktu")
# t
# ('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')

seq = sequence_class(immutable=False)
t = seq("Timbuktu")
# t
# ['T', 'i', 'm', 'b', 'u', 'k', 't', 'u']


def sequence_new_class(immutable):
    return tuple if immutable else list

