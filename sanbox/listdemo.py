s = "split this sentence into words".split()
print(s)

# index from front
print(s[2])

# index from end
print(s[-3])

# slicing
# slice range is half-open - stop not included
print(s[1:4])

# omitting the stop index slices to the end
print(s[2:])

# slices from front to third index not including 3
print(s[:3])

# full slice
# this idiom is useful for copying a list
print(s[:])
new_list = s[:]
print("new_list = {}".format(new_list))

# other ways of copying a list
use_copy = s.copy()
print("use_copy = {}".format(use_copy))

use_list = list(s)
print("use_list = {}".format(use_list))

# NOTE: all these list copy does shallow copies
print()
a = [[1,2],[3,4]]
print("a = {}".format(a))
b = a[:]
print("b = {}".format(b))

print("a == b is {}".format(a==b))
print("a[0] is b[0] is {}".format(a[0] is b[0]))

a[0] = [8,9]
print("a[0]= {}".format(a[0]))
print("b[0]= {}".format(b[0]))
a[1].append(5)
print("a[1]= {}".format(a[1]))

# list repetition
print("list repetition")
c = [22,34]
d = c * 5
print(d)

# NOTE: all repetition is shallow

print("finding elements in a list")
w = "some random string of text".split()
print(w)
print("index of string = {}".format(w.index('string')))
# print(w.index('badinput')) # will throw ValueError exception

print("list concatenation")
m = [1,2,3]
n = [4,5,6]
k = m + n
print("m = {}".format(m))
print("m = {}".format(n))
print("k = m+n : {}".format(k))
k.extend([33,44,55])
print("extended k: {}".format(k))

print("list reverse in place")
g = [1,11,21,1233,33,4566,334553]
print("g = {}".format(g))
g.reverse()
print("g(reversed) = {}".format(g))

s = [2,-3,44,12,54,32,123,454,32]
print("s = {}".format(s))
s.sort()
print("s(sorted) = {}".format(s))

print("use of built in sorted()")
x = [2,4,1,32,67]
y = sorted(x)
print("x = {}".format(x))
print("y(sorted from x) = {}".format(y))

print("use of reversed()")
p = [3,5,7,8,9]
q = reversed(p)
print("p = {}".format(p))
print("q(reversed p) = {}".format(q)) # this returns a reverse iterator
# we need to wrap it with list to see its contents
print("q(wrapped with list) = {}".format(list(q)))

