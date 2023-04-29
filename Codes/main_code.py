# This Python file has the entire code without particular libraries.
# Made by: Feltrim
# Instagram: instagram.com/vfeltrim_

# Libraries

from math import factorial, sqrt
from time import sleep


# Interface functions:

def line(size=42):
    """_summary_

    Args:
        size (int, optional): Defaults to 42.

    Returns:
        _type_: _Return '-'_
    """
    return '-' * size


def header(txt):
    """_summary_

    Args:
        txt (_type_): _txt = text provided to create headers_
    """
    print(line())
    print(txt.center(42))
    print(line())


def read_int(msg):
    """_summary_

    Args:
        msg (_type_): _msg = integer number_

    Returns:
        _type_: _if n == int, return n_
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: please, digit an valid argument.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUser chose not to enter this number.\033[m')
            return 0
        else:
            return n


def menu(options):
    """_summary_

    Args:
        options (_type_): options = text provided to create a menu with options_

    Returns:
        _type_: _a menu with all the options provided during coding_
    """
    header('Select the operation')
    c = 1
    for item in options:
        print(f'\033[34m{c}\033[m - \033[33m{item}\033[m')
        c += 1
    print(line())
    opt = read_int('\033[32mYour option\n>>>>> \033[m')
    return opt


# Operations functions:

def add(a=0, b=0):
    """_summary_

    Args:
        a (int, optional): _integer number provided by the user_. Defaults to 0.
        b (int, optional): _another integer number provided by the user_. Defaults to 0.

    Returns:
        _type_: _calculation result_
    """
    res = a + b
    return header(f'>>>>> \033[1;33m{a} + {b}\033[m = \033[1;34m{res}\033[m')


def sub(a=0, b=0):
    """_summary_

    Args:
        a (int, optional): _integer number provided by the user_. Defaults to 0.
        b (int, optional): _another integer number provided by the user_. Defaults to 0.

    Returns:
        _type_: _calculation result_
    """
    res = a - b
    return header(f'>>>>> \033[1;33m{a} - {b}\033[m = \033[1;34m{res}\033[m')


def mult(a=0, b=0):
    """_summary_

    Args:
        a (int, optional): _integer number provided by the user_. Defaults to 0.
        b (int, optional): _another integer number provided by the user_. Defaults to 0.

    Returns:
        _type_: _calculation result_
    """
    res = a * b
    return header(f'>>>>> \033[1;33m{a} x {b}\033[m = \033[1;34m{res}\033[m')


def div(a=0, b=0):
    """_summary_

    Args:
        a (int, optional): _integer number provided by the user_. Defaults to 0.
        b (int, optional): _another integer number provided by the user_. Defaults to 0.

    Returns:
        _type_: _calculation result_
    """
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
    """_summary_

    Args:
        a (int, optional): _integer number provided by the user_. Defaults to 0.
        b (int, optional): _another integer number provided by the user_. Defaults to 0.

    Returns:
        _type_: _calculation result_
    """
    res = a ** b
    return header(f'>>>>> \033[1;33m{a}^{b}\033[m = \033[1;34m{res}\033[m')


def square_root(a=0):
    """_summary_

    Args:
        a (int, optional): _integer number provided by the user_. Defaults to 0.

    Returns:
        _type_: _calculation result_
    """
    res = sqrt(a)
    if res.is_integer():
        return header(f'>>>>> \033[1;33m√{a}\033[m = \033[1;34m{res:.0f}\033[m')
    else:
        return header(f'>>>>> \033[1;33m√{a}\033[m = \033[1;34m{res}\033[m')


def fac(a=0):
    """_summary_

    Args:
        a (int, optional): _integer number provided by the user_. Defaults to 0.

    Returns:
        _type_: _calculation result_
    """
    res = factorial(a)
    return header(f'>>>>> \033[1;33m{a}!\033[m = \033[1;34m{res}\033[m')


# Main code, where we put all the functions together:

header('Python Calculator')

while True:
    n1 = read_int('Enter an integer\n>>>>> ')
    opt1 = menu(['Addition', 'Subtraction', 'Multiplication',
                'Division', 'More Options', 'Close the Program'])
    if opt1 == 1:
        n2 = read_int(f'>>>>> {n1} + ')
        add(n1, n2)
    elif opt1 == 2:
        n2 = read_int(f'>>>>> {n1} - ')
        sub(n1, n2)
    elif opt1 == 3:
        n2 = read_int(f'>>>>> {n1} x ')
        mult(n1, n2)
    elif opt1 == 4:
        n2 = read_int(f'>>>>> {n1} ÷ ')
        div(n1, n2)
    elif opt1 == 5:
        opt2 = menu(['Exponentiation', 'Square Root',
                    'Factorial', 'Close the Program'])
        if opt2 == 1:
            n2 = read_int(f'>>>>> {n1}^')
            exp(n1, n2)
        elif opt2 == 2:
            square_root(n1)
        elif opt2 == 3:
            fac(n1)
        elif opt2 == 4:
            header('Finishing....')
            sleep(1.5)
            header('''Thanks for using my program!!
Developed by:\033[1;96m Feltrim\033[m''')
            sleep(5)
            break
        else:
            print('\033[31mPlease, select a valid option.\033[m')

    elif opt1 == 6:
        header('Finishing....')
        sleep(1.5)
        header('''Thanks for using my program!!
Developed by:\033[1;96m Feltrim\033[m''')
        sleep(5)
        break
    else:
        print('\033[31mPlease, select a valid option.\033[m')
