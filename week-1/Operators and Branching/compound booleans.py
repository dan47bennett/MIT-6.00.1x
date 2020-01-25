# example of compound boolean

x = int(input('Enter integer 1: '))
y = int(input('Enter integer 2: '))
z = int(input('Enter integer 3: '))

if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')