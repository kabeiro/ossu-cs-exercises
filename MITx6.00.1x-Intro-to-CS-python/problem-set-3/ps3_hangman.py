# Hangman game
#

# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = True
    secretWordList = list(secretWord)
    for letter in secretWordList:
        if letter not in lettersGuessed:
            guessed = False
    return guessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    secretWordList = list(secretWord)
    for letter in secretWordList:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += '_ '
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letterList = list(string.ascii_lowercase)
    availableLetters = ''
    for letter in letterList:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long.')

    guesses = 8
    lettersGuessed = []
    guessed = False

    while guesses > 0:
        print('-------------')
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        guess = guess.lower()

        if guess not in lettersGuessed and guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))

        elif guess not in lettersGuessed and guess not in secretWord:
            lettersGuessed.append(guess)
            guesses -= 1
            print("Oops! That letter is not in my word: " +
                  getGuessedWord(secretWord, lettersGuessed))

        else:
            print("Oops! You've already guessed that letter: " +
                  getGuessedWord(secretWord, lettersGuessed))

        guessed = isWordGuessed(secretWord, lettersGuessed)
        if guessed:
            break
    print('-------------')
    if guessed:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
