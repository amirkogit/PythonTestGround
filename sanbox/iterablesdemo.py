print("iterables and iterator demo")

iterable = ['spring','summer','autumn','fall']
print(iterable)

iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# following will throw an exception
#print(next(iterator))

# small utility to make use of iter...
def get_first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

seasons = ['spring','summer','autumn','fall']
print("First season = {}".format(get_first(seasons)))

try:
    print("Empty iterable = {}".format(get_first(set()))) # throws exception
except ValueError as e:
    print(str(e))
