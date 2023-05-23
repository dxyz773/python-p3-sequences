#!/usr/bin/env python3


def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        num = 0
        prev = 0
        current = 1
        my_fib = [prev, current]
        while num < length:
            moment = prev + current
            my_fib.append(moment)
            prev = current
            current = moment
            num += 1
        if length <= 10:
            print(my_fib[0:10])
        else:
            print(my_fib)


print_fibonacci(10)
