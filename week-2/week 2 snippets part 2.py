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


# iterative gcd function
        

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        return a
    if a > b:
        gcd = b
        for i in range(b):
            if a % gcd == 0 and b % gcd == 0:
                return gcd
            else:
                gcd -= 1
    if a < b:
        gcd = a
        for i in range(b):
            if a % gcd == 0 and b % gcd == 0:
                return gcd
            else:
                gcd -= 1


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


# recursive Fibonacci

def fibonacci(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


# recursive palindrome detection

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        charString = ''
        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz":
                charString = charString + char
        return charString
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))


# search for character in string recursively

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1 and aStr != char:
        return False
    middleIndex = int(len(aStr) / 2)
    middleCharacter = aStr[middleIndex]
    if middleCharacter == char:
        return True
    if char < middleCharacter:
        return isIn(char, aStr[:middleIndex])
    if char > middleCharacter:
        return isIn(char, aStr[middleIndex:])


