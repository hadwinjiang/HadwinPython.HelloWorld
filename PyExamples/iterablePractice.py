Types of comprehensions
    list comprehensions
    set comprehensions
    dictionary comprehensions

Style
    declarative
    functional

readable
expressive
effective

// List
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
[len(word) for word in words]    

lengths = []
for word in words:
    lengths.append(len(word))

from math import factorial
f = [len(str(factorial(x))) for x in range(20)]

// set - use { } instead of [ ]
from math import factorial
f = {len(str(factorial(x))) for x in range(20)}

// dictionary
from pprint import pprint as pp
country_to_capital = {'United Kingdom': 'London',
        'Brazil': "Brazilia",
        'Morocco': 'Rabat',
        'Sweden': 'Stockholm'}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)

words = "hi hello foxtrot hotel".split()
{ x[0]: x for x in words }  

import os
import glob
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob
('*.py')} 
pp(file_sizes) 

from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True
[x for x in range(101) if is_prime(x)]

iterable protocol
    Iterable objects can be passed to the built-in iter() function to get an iterator
    iterator = iter(iterable)
iterator protocol
    Iterator objects can be passed to the built-in next() function to fetch the next item
    item = next(iterator)

iterable = ['Spring', 'Summer', 'Autumn', 'Winter'] 
iterator = iter(iterable)
next(iterator)
Traceback (most recent call last):                                          
  File "<stdin>", line 1, in <module>                                       
StopIteration                         

Generators in Python
* specify iterable sequences
    all generators are iterators
* are lazily evaluated
    the next value in the sequence is computed on demand
* can model infinite sequences
    such as data streams with no definite end
* are composable into pipelines
    for natural stream processing
def gen123():
    yield 1
    yield 2
    yield 3
    // return
g = gen123()
g
next(g)
for v in gen123():
    print(v)

Stateful generators
* Generators resume execution
* Can maintain state in local variables
* Complex control flow
* Lazy evaluation
def take(cout, iterable):
    "Take first count elements"
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item
def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

items = [5, 7, 7, 6, 5, 8]
for item in distinct(items):
    print(item)

Laziness and the infinite
def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b
for x in lucas()
    print(x)