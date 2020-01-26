# =============================================================================
# Problem 2
#
# Assume s is a string of lower case characters.
# 
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# =============================================================================

s = 'azcbobobegghakl'

count = 0

for charIndex in range(len(s) - 2):
    currentChar = s[charIndex]
    if currentChar == 'b':
        if s[charIndex + 1] == 'o' and s[charIndex + 2] == 'b':
            count += 1

print('Number of times bob occurs is: ' + str(count))