# This Python file has the main code with soma particular libraries to make it clean.
# Made by: Feltrim
# Instagram: instagram.com/vfeltrim_

# Libraries

from code_with_libraries.lib.operations import *
from time import sleep

# Main code, where we put all the functions together

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
