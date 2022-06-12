from math import sqrt


def Fib1(n: int):
    return int((1/sqrt(5))*(((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n))

def Fib2(n: int):
    return Fib2(n-1) + Fib2(n-2) if n > 1 else n

def Fib3(n: int):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

if __name__ == "__main__":
    print(Fib1(10))
    print(Fib2(10))
    print(Fib3(10))