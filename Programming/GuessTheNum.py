#!/usr/bin/env python3
def guess_number(n):
    while True:
        guess = int(input('Enter a number: '))
        if guess < n:
            print('Your number is too low')
            continue
        elif guess > n:
            print('Your number is too high')
            continue
        elif guess == n:
            print('Win')
            break
    return
guess_number(23)
