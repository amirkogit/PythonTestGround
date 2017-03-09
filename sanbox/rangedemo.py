# ranges are "half-open" - start is included but stop is not
for i in range(5):
    print(i)

# stop value of a range used as start value of consecutive range
a = list(range(5,20))
print(a)

b = list(range(10,15))
print(b)

# optional third step value
c = list(range(0,10,2))
print(c)

# not using range - enumerate
# enumerate() yields(index,value) tuples
print()
d = [6,44,56,1487,4556656,4478]
for p in enumerate(d):
    print(p)

# above code can be used even better by combining with a tuple unpacking
print()
for i, v in enumerate(d):
    print("i = {}, v = {}".format(i,v))