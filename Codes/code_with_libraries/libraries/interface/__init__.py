# This Python file has all the interface functions.
# Made by: Feltrim
# Instagram: instagram.com/vfeltrim_

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
