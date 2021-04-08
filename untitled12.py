

def fibonacciA(n):
    a = 0
    b = 1
    k=1
    for k in range(n):
        if (b <= n):
           c = b+a
           a = b
           b = c
    return b

fibonacciA(5)


def fibonacciB(n):
    a = 0
    b = 1
    k=1
    for k in range(n):
        c = b+a
        a = b
        b = c
        
    return b

fibonacciB(9)


def fibonacciC(limiteInf, limSup):
    a = 0
    b = 1
    k=1
    suma = 0
    for k in range(limSup):
        c = b+a
        a = b
        b = c
        if (k >= limiteInf and k <= limSup):
            suma = suma + b
    return suma

fibonacciC(3,6)



















