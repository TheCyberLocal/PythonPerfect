# all information about this file
"""
Author: Timothy Macfarlane
Purpose: To demonstrate how a properly written python file should look
How:/
To show how a program should be written this program will be written/
properly so the user can overview the file structure and learn the/
proper way to format and label functions and files in python.
"""

# Only import necessary submodules
# example (from cProfile import run as cRun) not (import cProfile)
from cProfile import run as cRun
from timeit import timeit as tRun
from random import randint as rint
from textwrap import wrap


def main():
    func1()


def func1():
    """
    Purpose: It creates the bucket string
    How:/
    By iterating through a range and adding to/
    the bucket var each time using randint
    Input: None
    Output: None
    """
    bucket = ""
    for i in range(300):
        bucket += str(rint(0, 9))
    bucket = subFunc1(bucket)
    subFunc2(bucket)


def func1_runnerUp():
    """
    Purpose: It creates the bucket string
    How:/
    By iterating through using a while statement and/
    adding to the bucket var each time using randint
    Input: None
    Output: None
    """
    bucket = ""
    counter = 0
    while counter < 300:
        counter += 1
        bucket += str(rint(0, 9))
    del counter  # remove variables no longer needed for cleaner memory
    bucket = subFunc1(bucket)
    subFunc2(bucket)


# Sub functions are like functions, but they don't complete a whole task
# There job is to compliment a function, so it can be cleaner and easier to read

# The purpose of having runnerUp functions is you can run time tests and try
# running tests to improve a single function without creating a whole new program copy

def subFunc1(txt):
    """
    Purpose: To clean bucket of odd numbers
    How:/
    By creating updating the old bucket with a sorted/
    list compression of only even numbers
    Input: bucket, str
    Output: ''.join(txt), str
    """
    txt = list([x for x in txt if (int(x) % 2 == 0)])
    return ''.join(txt)


def subFunc1_runnerUp(txt):
    """
    Purpose: To clean bucket of odd numbers
    How:/
    By creating new bucket and iterating through the old bucket/
    and adding even numbers to the new bucket then deleting old bucket
    Input: bucket, str
    Output: ''.join(temp), str
    """
    txt = list(txt)
    temp = []
    for i in txt:
        if int(i) % 2 == 0:
            temp.append(i)
    return ''.join(temp)


def subFunc2(txt):
    """
    Purpose: To format and # print results
    How:/
    By printing 50 at a time per line
    Input: bucket, str
    Output: None
    """
    while len(txt) > 50:
        # print(txt[:50])
        txt = txt[50:]
    # print(txt)


def subFunc2_runnerUp(txt):
    """
    Purpose: To format and # print results
    How:/
    By printing 50 at a time per line
    Input: bucket, str
    Output: None
    """
    # print('\n'.join(wrap(txt, 50)))


main()
cRun("main")

print(tRun(func1, number=10000))
print(tRun(func1_runnerUp, number=10000))
