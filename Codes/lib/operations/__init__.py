from Codes.lib.interface import *
from math import factorial, sqrt


def add(a=0, b=0):
    res = a + b
    return header(f'>>>>> \033[1;33m{a} + {b}\033[m = \033[1;34m{res}\033[m')


def sub(a=0, b=0):
    res = a - b
    return header(f'>>>>> \033[1;33m{a} - {b}\033[m = \033[1;34m{res}\033[m')


def mult(a=0, b=0):
    res = a * b
    return header(f'>>>>> \033[1;33m{a} x {b}\033[m = \033[1;34m{res}\033[m')


def div(a=0, b=0):
    try:
        res = a / b

        if res.is_integer():
            return header(f'>>>>> \033[1;33m{a} ÷ {b}\033[m = \033[1;34m{res:.0f}\033[m')
        else:
            return header(f'>>>>> \033[1;33m{a} ÷ {b}\033[m = \033[1;34m{res}\033[m')

    except ZeroDivisionError:
        while b == 0:
            print('\033[31mERROR: A number can not be divided by 0 (zero).\033[m')
            b = read_int(f'>>>>> {a} ÷ ')
        res = a / b

        if res.is_integer():
            return header(f'>>>>> \033[1;33m{a} ÷ {b}\033[m = \033[1;34m{res:.0f}\033[m')
        else:
            return header(f'>>>>> \033[1;33m{a} ÷ {b}\033[m = \033[1;34m{res}\033[m')


def exp(a=0, b=0):
    res = a ** b
    return header(f'>>>>> \033[1;33m{a}^{b}\033[m = \033[1;34m{res}\033[m')


def square_root(a=0):
    res = sqrt(a)
    if res.is_integer():
        return header(f'>>>>> \033[1;33m√{a}\033[m = \033[1;34m{res:.0f}\033[m')
    else:
        return header(f'>>>>> \033[1;33m√{a}\033[m = \033[1;34m{res}\033[m')


def fac(a):
    res = factorial(a)
    return header(f'>>>>> \033[1;33m{a}!\033[m = \033[1;34m{res}\033[m')
