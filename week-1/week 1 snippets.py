# example of conditionals

x = int(input('Enter an integer: '))

if x % 2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')


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
    

# example of a nested conditional

x = int(input('Enter an integer: '))

if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not 3')
elif x % 3 == 0:
        print('Divisible by 3 and not 2')
print('Done with conditional')


# example of 'guess and check' algorithm for integer cube numbers

x = int(input('Enter an integer: '))

ans = 0
while ans**3 < abs(x):
    ans += 1
if ans ** 3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))