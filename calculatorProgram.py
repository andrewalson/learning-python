print('Welcome, User.')
a = int(input('Please choose a menu option. Enter 1 for add, 2 for subtract, 3 for multiply, 4 for divide, 5 for raise to the power, 6 for modulus:'))

b = int(input('Please provide the first number.'))
c = int(input('Please provide the second number.'))

if a == 1: 
    print(b+c)

if a == 2: 
    print(b-c)

if a == 3:
    print(b*c)

if a == 4:
    if c == 0:
        print('Cannot divide by zero.')
    else:
        print(b/c)

if a == 5:
    print(b**c)

if a == 6:
    print(b%c)