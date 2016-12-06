from __future__ import division
from __future__ import print_function
import sys

# print the name of subdomain
def print_info():
    print ("Running Subdomain --> Introduction")
    
# if else demo
def ifelse_demo():
    print ("Enter a number")
    N = int(raw_input().strip())

    if N % 2 == 1:
        print ("Weird")
    elif N % 2 == 0 and 2 <= N <= 5:
        print ("Not Weird")
    elif N % 2 == 0 and 6 <= N <= 20:
        print ("Weird")
    else:
        print ("Not Weird")


# reading raw input
def read_raw_input():
    s = raw_input()
    print(s)

# arithmetic operators
def airthmetic_operators():
    print ("Enter two numbers a and b in a newline.")
    a = int(raw_input())
    b = int(raw_input())
    print (a + b)
    print (a - b)
    print (a * b)

# python division
def python_division():
    print ("Enter two numbers a and b in a newline.")

    # Enter your code here. Read input from STDIN. Print output to STDOUT
    a = int(raw_input())
    b = int(raw_input())

    # print integer division
    print (a // b)

    # print float division
    print (a / b)

# simple loop demo
def simple_loop():
    print ("Enter a number n. Will print the squares of numbers between 0 and n")
    n = int(raw_input())
    for i in range(0,n):
        print (i * i)

# print function
def print_function():
    n = int(raw_input())
    for i in range(1,n):
        print (i,end = '')

# Write a function
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# calling a function to check leap year
def check_leap_year_demo():
    year = int(raw_input())
    print (is_leap(year))

def generate_input_min_index_diff():
    import random
    # generate input for minimum index difference problem
    arr_size = 20
    arr1 = []
    arr2 = []
    [arr1.append(x) for x in range(arr_size)]
    random.shuffle(arr1)

    file = open('c:\\temp\\q1_input_20.txt','w')
    file.write("%d\n" %arr_size)
    for i in arr1:
        file.write("%d " %i)
    file.write("\n")

    arr2 = arr1
    random.shuffle(arr2)
    for i in arr2:
        file.write("%d " %i)
    file.close()

