print("generators demo")

def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(g)

print(next(g))
print(next(g))
print(next(g))

# will issue StopIteration exception
#print(next(g))

print()
for v in gen123():
    print(v)

h = gen123()
i = gen123()

print(h)
print(i)

print(next(h))
print(next(h))
print(next(i))

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6

g = gen246()
print(next(g))
print(next(g))
print(next(g))

# stateful generators
print("stateful generators...")
def read_stream(count,iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def run_read_stream():
    items = [2,4,5,2,7,9]
    for item in read_stream(3,items): # will read only 3 values from the provided list
        print(item)

run_read_stream()

# generator that keeps track of which elements are read
def read_distinct_stream(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_read_distinct_stream():
    items = [5,7,7,6,5,5]
    for item in read_distinct_stream(items):
        print(item)

print("run distinct stream...")
run_read_distinct_stream()

# running two different generators to create a lazy pipeline
# reading first 3 distinct items from the list
def run_pipeline():
    items = [1,6,6,6,3,5,6,7,2,3]
    for item in read_stream(3,read_distinct_stream(items)):
        print(item)

print("reading first 3 distinct items from the list")
run_pipeline()

# any demo
print(any([False,False,True]))
print(all([False,False,True]))

# zip demo
# suppose two temperature readings for two days
sunday = [12,45,34,31,67,23,90]
monday = [22,35,44,51,87,13,50]

for item in zip(sunday,monday):
    print(item)

for sun,mon in zip(sunday,monday):
    print("average = ",(sun + mon) / 2)

tuesday = [32,55,74,81,27,93,20]

for temps in zip(sunday,monday,tuesday):
    print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(
        min(temps), max(temps), sum(temps)/len(temps)
    ))

# chain demo
from itertools import chain
temperatures = chain(sunday,monday,tuesday)
print(temperatures)
print(type(temperatures))
result = all(t > 0 for t in temperatures)
print(result)


