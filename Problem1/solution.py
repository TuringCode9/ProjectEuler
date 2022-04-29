#!/usr/bin/env python3

def SumaMul3or5(n):
    x = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            x += i # x = x + i
    return x

result = SumaMul3or5(1000)
print(result)


