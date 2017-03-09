print("comprehensions demo")

# list comprehensions
# general form of list comprehension is;
# [expr(item) for item in iterable]
words = "some random text is included here with this sentence".split()
print(words)
word_length = [len(word) for word in words]
print("length of each word = {}".format(word_length))

# above is equivalent to the following
lengths = []
for word in words:
    lengths.append(len(word))

print(lengths)

from math import factorial
f = [str(factorial(x)) for x in range(20)]
print("factorial of range(20) = {}".format(f))
l = [len(str(factorial(x))) for x in range(20)]
print("length of factorial digits for range(20):")
print(l)

# set comprehensions
# general form:
# {expr(item) for item in iterable}
from pprint import pprint as pp
s = {len(str(factorial(x))) for x in range(20)}
print("set comprehension result")
print(s)

# dictionary comprehension
#{key_expr:value_expr for item in iterable}
states_to_initial = {'california' : 'ca',
                     'florida': 'fl',
                     'arizona':'az',
                     'iowa':'ia'}
pp(states_to_initial)

# to reverse the mapping from initial to states name
initial_to_states = {initial:states for states,initial in states_to_initial.items()}
pp(initial_to_states)

# print all the primes less than 100
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(sqrt(x))+ 1):
        if x % i == 0:
            return False
    return True

primes_less_than_100 = [x for x in range(101) if is_prime(x)]
print("all primes less than 100")
print(primes_less_than_100)

