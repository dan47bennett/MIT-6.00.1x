# introduction of functions

def isEven(number):
    """
    
    Parameters
    ----------
    number : int
        a positive integer

    Returns
    -------
    True if number is even, False otherwise

    """
    print("hi")
    return number % 2 == 0


# example of iteration

def multiplyIteratively(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


# example of recursion

def multiplyRecursively(a, b):
    if b == 1:
        return a
    else:
        return a + multiplyRecursively(a, b - 1)


# iterative power function

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


# recursive power function

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)




# towers of hanoi code

def printMove(origin, destination):
    print('Move from ' + str(origin) + ' to ' + str(destination))

def towers(n, origin, destination, spare):
    if n == 1:
        printMove(origin, destination)
    else:
        towers(n - 1, origin, spare, destination)
        towers(1, origin, destination, spare)
        towers(n - 1, spare, destination, origin)


