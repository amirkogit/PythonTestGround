print("dict demo")
names_and_ages = [('bob',2),
                  ('jack',34),
                  ('mike',33),
                  ('paul',21)]

# dict() constructor with iterable series of key-value 2 tuples
d = dict(names_and_ages)
print(d)

# keyword arguments- requires keys are valid python identifiers
d = dict(fl = 'florida', ca = 'california', az = 'arizona')
print(d)

# copying of dict is shallow
copy_d = d.copy()
print(copy_d)

dict_d = dict(d)
print(dict_d)

# updating dictionary
namesages = dict(names_and_ages)
print(namesages)

namesages.update(d)
print(namesages)

# iteration
states = dict(fl = 'florida', ca = 'california', az = 'arizona')
print(states)
for key in states:
    print("{key} ==> {value}".format(key=key, value = states[key]))

# use values() for an iterable view onto the series of values
for value in states.values():
    print(value)

for key in states.keys():
    print(key)

# use items() for an iterable view onto the series of key-value tuples
# use with tuple unpacking
for key,value in states.items():
    print("{key} ==> {value}".format(key=key, value=value))

# the in and not in operators work on the keys
print('az' in states)
print('ut' in states)

# dict is mutable
# keys must immutable, values may be mutable and the dictionary itself is mutable
mass = {'H': [1,2,3],
        'He':[3,4],
        'C':[10,22],
        'B': [7,9,10]
        }
print(mass)
mass['H'] += [6,8,9,11] # here list is extended for 'H' but the key is not changed
print(mass)

mass['N'] = [5,7,8,11,23,44,55]
print(mass)

# using pretty printing
from pprint import pprint as pp
pp(mass)