print("set demo")
from pprint import pprint as pp
a = {3,2,44,22,88,45,3452,43290,8965}
pp(a)
print(a)
print(type(a))

# empty{} makes a dict, so for empty set creation use set() constructor
b = {}
print(type(b))

c = set()
print(type(c))

# set() constructor accepts: iterable series of values
# duplicates are discarded
d = set([1,3,4,5,1,2,7,3,2,4,8,9,0,12])
print(d)

# sets are iterable: order is arbitary
for x in {1,2,4,6,7,9,12,34}:
    print(x)

# membership/containment
color = {'red','blue','green','cyan'}
print(color)
print("check red : {}".format('red' in color))
print("check black: {}".format('black' in color))
print("check yellow: {}".format('yellow' not in color))

# adding elements
color.add('black')
color.add('brown')
print(color)

# adding multiple elements
color.update(['navy','crimson', 'white'])
print(color)

# removing elements
color.remove('white')
print(color)

color.discard('white')
print(color)

# copy
copy_color = color.copy()
print("copy_color = {}".format(copy_color))

copy_color2 = set(color)
print("copy_color2 = {}".format(copy_color2))

