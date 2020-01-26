# =============================================================================
# Problem 3
# 
# Assume s is a string of lower case characters.
# 
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# 
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.

# For example, if s = 'abcbcd', then your program should print
# 
# Longest substring in alphabetical order is: abc
# =============================================================================

s = 'azcbobobegghakl'


wordLength = len(s)
longestAlphabetical = ''

for end in range(wordLength + 1):
    for start in range(end + 1):
        subString = s[start : end]
        if subString == ''.join(sorted(subString)) and len(subString) > len(longestAlphabetical):
            longestAlphabetical = subString
        

print('Longest substring in alphabetical order is: ' + str(longestAlphabetical))