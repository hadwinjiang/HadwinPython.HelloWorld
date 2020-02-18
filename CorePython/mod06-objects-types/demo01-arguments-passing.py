m = [9, 15, 24]


def modify(k):
    k.append(39)
    print("k=", k)


modify(m)
print(m)

# all modified to [9, 15, 24, 39]

f = [14, 23, 37]


def replace(g):
    g = [17, 28, 45]
    print("g=", g)


replace(f)  # [17, 28, 45]
print(f)  # [14, 23, 37]
