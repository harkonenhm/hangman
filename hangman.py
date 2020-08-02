import random
import string

#functions
def printWord(word):
    for letter in word:
        print(letter, " ", end="")
    print()

def changeWord(letter):
    for i, value in enumerate(word):
        if (letter == word[i]):
            maskedWord[i] = letter

f = open("hangman_words.txt", mode="r")
contents = f.read()

#variables
words = contents.split()
selectedWord = words[random.randint(0, len(words)-1)]
word = list(selectedWord)
maskedWord = ["_"] * len(word)
availableLetters = list(string.ascii_lowercase)
wrongGuessCounter = 0
correctGuessCounter = len(set(word))


#game logic
print("Welcome to play Hangman!")
print("Try to guess following word:")
while (True):
    printWord(maskedWord)
    
    print("Available letters:")
    printWord(availableLetters)
    print("Wrong guesses left:", (10 - wrongGuessCounter))
    print("Pick a letter or type exit to close the game: ")
    guess = input()
    if(guess == 'exit'):
        print("See you later!")
        break
    #valid guess
    elif (guess in availableLetters):
        availableLetters.remove(guess)
        if (guess in word):
            print("Correct!")
            correctGuessCounter = correctGuessCounter - 1
            changeWord(guess)
        else:
            print("Wrong letter!")
            wrongGuessCounter = wrongGuessCounter + 1
    #invalid guess
    elif (len(guess) > 1 or not guess.isalpha()):
        print("Pick one available letter.")        
    #already used letter
    else:
        print("You already guessed that letter. Pick a different one!")    
    
    #check win & lose conditions
    if(wrongGuessCounter == 10):
        print("You lost!")
        print("Word was:")
        printWord(word)
        break
    elif (correctGuessCounter == 0):
        printWord(word)
        print("You won!")
        break