# returns a tuple value
def minmax(items):
    return min(items), max(items)


def main():
    lower, upper = minmax([56,45,11,8,7,66,987])
    print("Min: {} Max: {}".format(lower,upper))

    point = tuple([1,2])
    print("point as tuple: {}".format(point))

    line2d = tuple([(1,2),(3,4)])
    print("line points as tuple: {}".format(line2d))


if __name__ == "__main__":
    main()