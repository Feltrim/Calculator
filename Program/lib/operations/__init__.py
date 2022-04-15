from lib.interface import *
from math import factorial, sqrt


def add(a=0, b=0):
    res = a + b
    return header(f'>>>>>\033[1;33m{a} + {b}\033[m = \033[1;34m{res:.0f}\033[m')


def sub(a=0, b=0):
    res = a - b
    return header(f'>>>>>\033[1;33m{a} - {b}\033[m = \033[1;34m{res:.0f}\033[m')


def mult(a=0, b=0):
    res = a * b
    return header(f'>>>>>\033[1;33m{a} x {b}\033[m = \033[1;34m{res:.0f}\033[m')


def div(a=0, b=0):
    res = a / b
    if a % b == 0:
        return header(f'\033[1;33m{a} ÷ {b}\033[m = \033[1;34m{res:.0f}\033[m')
    else:
        return header(f'\033[1;33m{a} ÷ {b}\033[m = \033[1;34m{res:.2f}\033[m')

def exp(a=0, b=0):
    res = a ** b
    return header(f'\033[1;33m{a}^{b}\033[m = \033[1;34m{res:.0f}\033[m')

def sqrtt(a=0):
    res = sqrt(a)
    if res.is_integer():
        return header(f'\033[1;33m√{a}\033[m = \033[1;34m{res:.0f}\033[m')
    else:
        return header(f'\033[1;33m√{a}\033[m = \033[1;34m{res}\033[m')

def fac(a):
    res = factorial(a)
    return header(f'\033[1;33m{a}!\033[m = \033[1;34m{res:.0f}\033[m')
