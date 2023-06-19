# calculator
print('press 1 for addition')
print('press 2 for multiplication')
print('press 3 for subtraction')
print('press 4 for division')

while True:
    operation = input('Enter the operation: ')

    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    if operation == '1':
        c = a+ b
        print(c)

    elif operation == '2':
        c = a*b
        print(c)

    elif operation == '3':
        c = a-b
        print(c)

    elif operation == '4':
        c = a/b
        print(c)

    else:
        print('invalid operation perform')
        break
    