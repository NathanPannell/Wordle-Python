import random

# Number of allowed guesses
MAX_TRIES = 6

# Emoji icons used to represent correct/incorrect characters
GREEN_TILE = '🟩'
YELLOW_TILE = '🟨'
GREY_TILE = '⬛'

# Thank you to cfreshman on github for providing well organized data for me to use :)
# Guesses: ~12000 5-letter words
# Answers: ~2000 common 5-letter words
# The answer should always be a somewhat common word. The program will accept all 12000 5-letter english words as valid guesses.
GUESSES = 'guesses.txt'
ANSWERS = 'answers.txt'

def game() -> None:
    '''
    1. Initializes variable and selects a word from answers_list
    2. Loops {MAX_TRIES} times, asking the user to enter a word
    3. In each loop, prints out coloured tiles as feedback depending on which letters in the guess correspond to the answer
    ---RULES---
    If char is nowhere in answer, print grey tile
    If char is in the correct spot, print green tile
    If char is in incorrect spot but appears somewhere in the answer, print yellow tile

    ---DUPLICATE CHARACTERS---
    If multiple of the same char are guessed, only return as many green/yellow tiles as there are matching characters in the answer
    Ex.
    guess = 'apple'
    answer = 'poppy'
    print('⬛🟨🟩⬛⬛')
    both p's can be mapped to different chars in the answer

    guess = 'poppy'
    answer = 'apple'
    print('🟨⬛🟩⬛⬛')
    two of the p's are given positive feedback, but there is no third in the answer. This means the third p is given a grey tile
    '''
    # Initialization and answer selection
    tries = 0
    answer = answers_list[random.randrange(0,len(answers_list)-1)]

    # Generates a dictionary containing characters and their frequency (for the answer)
    answer_letters = {}
    for char in answer:
        addToDict(char, answer_letters)

    # Start of guessing loop
    print('Make a guess:\n')
    while tries < MAX_TRIES:
        # Per loop initialization and iteration (tries)
        tries += 1
        tiles = GREY_TILE * 5
        matches = {}

        # Collect player input for guess
        guess = getInputInGuesses('')

        # Analyze guess for exactly matching answers (Green tiles)
        # Perfect matches have priority over partial matches
        # If there are multiple correct matches, extra partial matches shouldn't show up
        for i in range(5):
            if answer[i] == guess[i]:
                tiles = changeCharAtIndex(GREEN_TILE, i, tiles)
                addToDict(answer[i], matches)
        
        # Analyze partial matches (Yellow tiles)
        for i in range(5):
            char = guess[i]
            if char in answer_letters:
                # If there were no previous matches for char, add a yellow tile and initialize entry to 1
                if char not in matches:
                    matches[char] = 1
                    tiles = changeCharAtIndex(YELLOW_TILE, i, tiles)

                # If there were previous matches for char, but there are still more chars in answer_letters
                # Add a yellow tile and iterate number of matches
                elif matches[char] < answer_letters[char]:
                    matches[char] += 1
                    tiles = changeCharAtIndex(YELLOW_TILE, i, tiles)

                # If every instance of char in answer has been matched already, further instances of char in guess are left grey

        print(tiles)

        # Checking for victory (after giving tiles feedback)
        if guess == answer:
            print(f'\nYou got it in {tries} tries! The word was {answer.upper()}.\n')
            return()

    # While loop breaks, therefore the player has reached the max number of guesses
    print(f'\nSorry, the word was {answer.upper()}.\n')

def addToDict(value, dictionary: dict) -> None:
    '''
    Mutates original frequency dictionary and adds new entry for the value or iterates frequency count if entry already exists
    '''
    if value in dictionary:
        dictionary[value] += 1
    else:
        dictionary[value] = 1

def changeCharAtIndex(character: str, index: int, string: str) -> str:
    '''
    Replace character at index in string with given character
    '''
    result = string[:index] + character + string[index+1:]
    return result

def getInputInGuesses(message: str) -> str:
    '''
    Repeatedly asks the user for input until they enter a word in the allowed guesses list
    Returns the valid guess as a string
    '''
    guess = input(message).lower()
    while guess not in guesses_list:
        guess = input(message)
    return guess
    
def readFile(filename: str) -> list[str]:
    '''
    Takes name of a text file and returns a list containing strings
    Each word is stripped of \n then added to the list
    '''
    output_list = []
    file_handle = open(filename, 'r')
    for line in file_handle:
        line = line.strip()
        output_list.append(line)
    file_handle.close()
    return output_list

if __name__ == '__main__':
    '''
    1. Reads guesses.txt and answers.txt to create lists for easy access
    2. Starts game() and loops while the user enters 'y' to play again
    3. Quits out of the program when user enters something other than 'y'
    '''
    # Initialization of word lists
    guesses_list = readFile(GUESSES)
    answers_list = readFile(ANSWERS)

    # Core game loop
    game()
    new_game = input('Play new game? (y/n): ')
    while new_game.lower() == 'y':
        game()
        new_game = input('Play new game? (y/n): ')
