def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    finalTuple = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            finalTuple += aTup[i],
    return finalTuple


# applying a function to each element in a list
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


# applying each function in a list to a variable
def applyFunctions(L, x):
    for f in L:
        print(f(x))