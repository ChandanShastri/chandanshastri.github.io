print("NKDWDEKWE")

def try_this () :
    print("YES")
a=10
try_this()

from functools import lru_cache

@lru_cache(maxsize=1000)
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
        return fib(n-1) + fib(n-2)




cache={}

def fib_man(n):
    if n in cache :
        return cache[n]
    elif n==1 :
        value = 1
    elif n==2 :
        value = 2
    elif n>2 :
        value = fib(n-1) + fib(n-2)
    cache[n]=value
    return value

for i in range (1,100) :
    print(fib_man(i))

