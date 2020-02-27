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


# create dictionary with frequency of each element in an array or word in a song, for example
def lyricsToFrequencies(lyrics):
    wordDictionary = {}
    for word in lyrics:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    return wordDictionary


# find 

sheLovesYou = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',
]

beatles = lyricsToFrequencies(sheLovesYou)

print(beatles)