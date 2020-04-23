#!/usr/bin/env python3
num = int(input("Input a number: "))
if ((num % 3 == 0) & (num % 5 == 0)):
    print('Fizzbuzz')
elif (num % 3 == 0):
    print('fizz')
elif (num % 5 == 0):
    print('buzz')
else:
    print(num)
