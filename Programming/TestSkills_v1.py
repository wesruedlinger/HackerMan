#!/usr/bin/env python3

def q1(floatstr):
    '''
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the
    argument as elements in the list.
    '''
    result = []
    for i in floatstr.split(','):
        result.append(float(i))
    return result

def q2(*args):
    '''
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''
    return (sum(args) / len(args))

def q3(lst,n):
    '''
    Given a list (lst) and a number of items (n), return a new
    list containing the last n entries in lst.
    '''
    result = lst[-n:]
    return result

def q4(strng):
    '''
    Given an input string, return a list containing the ordinal numbers of
    each character in the string in the order found in the input string.
    '''
    result = []
    for i in strng:
        result.append(ord(i))
    return result

def q5(strng):
    '''
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    a = strng.split()
    return tuple(a)

'''
def q6():
    Given an input string similar to the below, craft a regular expression
    pattern to match and extract the date, time, and temperature in groups
    and return this pattern. Samples given below.
    Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
    Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C

    pass'''

def q7(filename):
    '''
    Given a filename, open the file and return the length of the first line
    in the file excluding the line terminator.
    '''
    f = open(filename, 'r')
    c = f.readline()
    d = len(c.strip())
    return d

def q8(filename,lst):
    '''
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in
    the list. If "stop" is not found in the list, write the entire list to
    the file on separate lines.
    '''
    with open(filename, 'w') as fh:
        for i in lst:
            if i.lower() == "stop":
                break
            else:
                fh.write(i + "\n")
    return

def q9(miltime):
    '''
    Given the military time in the argument miltime, return a string
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    print(miltime)
    if miltime > 259 and miltime < 1200:
        greeting = "Good Morning"
    elif miltime > 1159 and miltime < 1600:
        greeting = "Good Afternoon"
    elif miltime > 1559 and miltime < 2100:
        greeting = "Good Evening"
    elif miltime > 2059 and miltime < 300:
        greeting = "Good Night"
    return greeting

def q10(numlist):
    '''
    Given the argument numlist as a list of numbers, return True if all
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    if all(i >= 0 for i in numlist):
        return True
    else:
        return False
