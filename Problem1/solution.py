#!/usr/bin/env python3

def SumaMult3or5(n):
    x = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            x += i # x = x + i
    return x

result = SumaMult3or5(1000)
print(result)


