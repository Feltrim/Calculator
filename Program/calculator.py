from lib.operations import *

header('Python Calculator')

n1 = read_int('Digit the first number\n>>>>> ')
n2 = read_int('Digit the second number\n>>>>> ')


while True:
    opt = menu(['Addition', 'Subtraction', 'Multiplication', 'Division', 'Select new numbers', 'Close the Program'])
    if opt == 1:
        add(n1, n2)
    elif opt == 2:
        sub(n1, n2)
    elif opt == 3:
        mult(n1, n2)
    elif opt == 4:
        div(n1, n2)
    elif opt == 5:
        n1 = read_int('Digit the first number\n>>>>> ')
        n2 = read_int('Digit the second number\n>>>>> ')
    elif opt == 6:
        header('''Thanks for using my program!!
Developed by:\033[1;96m Feltrim\033[m''')
        break
    else:
        print('\033[31mPlease, select a valid option.\033[m')
