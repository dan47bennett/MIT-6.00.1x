# while, if and in example

anLetters = "aefhilmnorsxAEFHILMNORSX"
word = input("Input a word: ")
times = int(input("Enthusiasm level: "))
i = 0

while i < len(word):
    char = word[i]
    if char in anLetters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1

print("What does that spell?")
for i in range(times):
    print(word, "!!!")


# example of square root bisection search

x = 25
epsilon = 0.01
numberOfGuesses = 0
low = 1.0
high = x
answer = (high + low) / 2.0

while abs(answer ** 2 - x) >= epsilon:
    print('low = ' + str(low) + 'high = ' + str(high) + 'answer = ' + str(answer))
    numberOfGuesses += 1
    if answer**2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low) / 2.0
print('numberOfGuesses = ' + str(numberOfGuesses))
print(str(answer) + ' is close to the square root of ' + str(x))



# create number guessing game
low = 0
high = 100
allowedLetters = 'hcl'
guess = int((low + high) / 2)
print("Please think of a number between 0 and 100!")
#answer = input("Is your secret number " + str(guess) + "? ")
answer = 'l'

while answer != 'c':
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate\
the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == 'h':
        high = int((low + high) / 2)
    if answer == 'l':
        low = int((low + high) / 2)
    if answer not in allowedLetters:
        print("Sorry, I did not understand your input.")
    guess = int((low + high) / 2)

print("Game over. Your secret number was: " + str(guess))

# Newton-Raphson method example

epsilon = 0.01
y = 25.0
guess = y / 2.0
numberOfGuesses = 0

while abs(guess * guess - y) >= epsilon:
    numberOfGuesses += 1
    guess = guess - ((guess ** 2 - y) / (2 * guess))
print("Number of guesses = " + str(numberOfGuesses))
print("Square root of " + str(y) + "is about " + str(guess))