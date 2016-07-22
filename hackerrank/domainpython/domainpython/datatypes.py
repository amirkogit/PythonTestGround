# print the name of subdomain
def print_info():
    print ("Running Subdomain --> Data Types")

def list_intro_basic():
    arr = list()
    arr = [1,2,3]
    print (arr)
    print (arr[0] + arr[1] + arr[2])
    arr.append(56)
    print arr
    arr2 = []
    arr2 = [-3, 22]
    print arr2
    arr.extend(arr2)
    print arr
    arr.insert(3,7)
    print arr

def list_intro():
    # initialize the empty list
    arr = []

    for i in range(int(raw_input())):
        commands = raw_input().split()

        for i in range(1,len(commands)):
            commands[i] = int(commands[i])

        if commands[0] == "append":
            arr.append(commands[1])
        elif commands[0] == "insert":
            arr.insert(commands[1],commands[2])
        elif commands[0] == "remove":
            arr.remove(commands[1])
        elif commands[0] == "pop":
            arr.pop()
        elif commands[0] == "index":
            arr.index(commands[1])
        elif commands[0] == "count":
            print (arr.count(commands[1]))
        elif commands[0] == "sort":
            arr.sort()
        elif commands[0] == "reverse":
            arr.reverse()
        elif commands[0] == "print":
            print(arr)

def tuples_intro():
    n = raw_input()
    t = tuple([int(i) for i in (raw_input().split())])
    print(hash(t))

def list_comprehensions():
    X = int(raw_input())
    Y = int(raw_input())
    Z = int(raw_input())
    N = int(raw_input())

    #empty list
    arr = []
    [ arr.append([x,y,z]) for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != N ] 
    print arr