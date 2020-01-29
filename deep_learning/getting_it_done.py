# from functools import lru_cache

# @lru_cache(maxsize=1000)
def fib(n):
    if n==1 :
        return 1
    elif n==2 :
        return 2
    elif n>2 :
        return fib(n-1) + fib(n-2)


def fib_vanilla(n):
    if n==1 :
        return 1
    elif n==2 :
        return 2
    elif n>2 :
        return fib_vanilla(n-1) + fib_vanilla(n-2)




cache={}

def fib_man(n):
    value=0
    if n in cache :
        #print("IN")
        return cache[n]
    if n==1 :
        value = 1
    elif n==2 :
        value = 2
    elif n>2 :
        value = fib_man(n-1) + fib_man(n-2)
    cache[n]=value
    #print(cache)
    return value

# for i in range (100) :
#     print(fib_man(i))
w=[1,2,3,4,5]
z=[1,3,4,5,6]
a=[(i,y) for i in w for y in z]
b=[i*4 for i in range (2,200)]
print(a,b)

import timeit

aa=timeit.timeit(stmt="(a,b,c)", number=1000)
print(aa)