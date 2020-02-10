test = ('I', 'am', 'a', 'test', 'tuple')


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


print(oddTuples(test))