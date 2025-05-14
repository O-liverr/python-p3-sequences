#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length <= 0:
        print([])
        return
    for i in range(length):
        if i == 0:
            fib_list.append(0)
        elif i == 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list)