import sys

print("exceptions demo")

def convert(s):
    x = -1
    try:
        x = int(s)
        print("conversion succeeded! x = ",x)
    except(ValueError,TypeError):
        print("Conversion error!")
    return x

def sqrt(x):
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

# this is wasteful!!
def sqrt2(x):
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess

def sqrt3(x):
    if x < 0:
        raise ValueError("Cannot compute for negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    print(convert('3'))
    print(convert('abc'))
    print(convert([1, 2, 3]))

    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ZeroDivisionError:
        print("Cannot compute for negative number")

    try:
        print("executed second try block")
        print(sqrt3(-1))
    except ValueError as e:
        print(e, file = sys.stderr)

    print("program executed normally!")

main()


