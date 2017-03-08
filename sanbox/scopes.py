"""
Demonstrates scopes
"""

count = 0

def show_count():
    print("count = ", count)


def set_count(c):
    global count # without using 'global' count is not updated
    count = c
