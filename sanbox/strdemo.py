"""
str demo
"""

fruits = ';'.join(['apples', 'oranges','banana'])
print(fruits)

splitted = fruits.split(';')
print(splitted)
print()

# fast way of concatenating a collection of strings
text = ''.join(['high','way','man'])
print(text)

# partition returns a tuple
my_str = "unforgetable".partition("forget")
print(my_str)

print()
log = "pelvis: Registration Point Timing: 336 milliseconds"
print(log)
pelvis, _, reg_time = log.partition(":")
print(pelvis)
print(reg_time)

# returned tuple from partition can be collected as tuple unpacking as follows
departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure)
print(separator)
print(arrival)

# format usage
# integer field names matched with positional arugments
msg = "The age of {0} is {1}".format('Jill',33)
print(msg)

# field names can be omitted if used in sequence
msg = "Age is {} for {}".format(34,'Jack')
print(msg)

# named fields are matched with keyword arguments
msg = "Current position is {latitude} {longitude}".format(latitude = "60N",
                                                          longitude = "5E")
print(msg)

# accessing values through keys or indexes with square brackets in the replacement field
pos = (22.3,0.336,85.45)
msg = "3D position is x = {pos[0]} y = {pos[1]} z = {pos[2]}".format(pos=pos)
print(msg)

# access attributes using dot in the replacement field
import math
msg = "Math constants: pi = {m.pi}, e = {m.e}".format(m=math)
print(msg)

# replacement field mini-language provides many values and alignment formatting options
msg = "Math constants: pi = {m.pi:.3f}, e = {m.e:.3f}".format(m=math)
print(msg)

# to get help on usage of str
# help(str)