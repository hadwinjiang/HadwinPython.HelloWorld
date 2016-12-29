tuple

def minmax(items):
    return min(items), max(items)

minmax([83,33,85,53,31,86])

lower, upper = minmax([83,33,85,53,31,86])

5 not in (3, 5, 17, 257, 65537)

str // help(str)

len("welcome")
"New" + "found"
s = "part1"
s += "part2"
s += "part3"
colors = ';'.join(['#45ff23', '#2321fa', '#1298a3', '#a32312'])
colors.split(';') // return a list
"unforgetable".partition("forget") // return a tuple
"The age of {0} is {1}".format('Jim', 32)

range
range(5) // stop
range(0,5)  // start stop
for i in range(5):
    print(i)
list(range(5,10))
list(range(0,10,2)) 
t = [6, 372, 8862, 12221, 21421]
for p in enumerate(t):
    print(p)
(0, 6)
(1, 372)
(2, 8862)

list
s = "show how to index into sequences".split()
s[4]
s[-5] // negative
s[1:4] // ["how", "to", "index"]
s[1:-1] // ['how', 'to', 'index', 'into']
s[3:] // ['index', 'into', 'sequence']
s[:3] // ['show', 'how', 'to']
s[:x] + s[x:] == s
full_slice = s[:]
u = s.copy()
v = list(s)
Copy are shallow

c=[21,37]
d=c*4
d // [21,37,21,37,21,37,21,37]
Repetition is Shallow
w = "the quick brown fox jumps over the lazy dog".split()
i = w.index('fox') //3
w[i] // 'fox'
w.count('the')  //2
del w[2]
w.remove('brown')
seq.insert(index, item)

k.reverse() 
g = [1, 11, 2, 1211, 112111]
g.reverse()
g.sort()
g.sort(reversed=True)
h.sort(key=len)
x = [4, 9, 2, 1]
y = sorted(x)
q = reversed(x)

dict
urls = {'Google': 'http://google.com', 
    'Pluralsight': 'http://pluralsight.com',
    'Sixty North': 'http://sixty-north.com',
    'Microsoft': 'http://microsoft.com'}
urls['Google']
// Key Must be immutable
// Value can be mutable
// Artibary order
names_and_ages = [('Alice',32), ('Bob', 48), ('Charlie', 28)]
d = dict(names_and_ages)
e = d.copy()
f = dict(d)
g = dict(wayne=44, tom=34)
f.update(g) // Extend
for key in colors:
    print("{key} => {value}".format(key=key, value=colors[key]))
for value in colors.values():
    print(value)
for key, value in colors.items():
    print("{key} => {value}")
from pprint import pprint as pp 
pp(m)

set
p = { 12, 33, 45, 23, 32}
e = set()
e = set([2, 3, 4, 5 , 6])
k.add(108)
k.update(2, 3, 4)
k.remove(2)
set1.union(set2)
set1.difference(set2)
set1.intersect(set2)
set1.symmetric_difference(set2)
set1.isdisjoint(set2)
set1.issubset(set2)
set2.issuperset(set2)

Container(in, not in): str, list, range, tuple, tytes, set, dict
Sized(len): str, list, range, tuple, bytes, set, dict
Iterable(for in): str, list, range, tuple, bytes, set, dict
Sequence([index]): str, list, range, tuple, bytes
Mutable Sequence: list
Mutable Set: set
Mutable Mapping: dict
