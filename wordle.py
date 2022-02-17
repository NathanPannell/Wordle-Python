import random, os

MAX_TRIES = 6
YES = "🟩"
IN = "🟨"
NO = "⬜"
GUESSES = "guesses.txt"
ANSWERS = "answers.txt"

os.chdir("C:\\Users\\Nate's Zenbook\\Documents\\Old Schoolwork\\Fall 2021\\CSC 110\\wordle")

def game():
    tries = 0
    answer = answers_list[random.randrange(0,len(answers_list)-1)]
    answer_letters = []
    for i in range(5):
        answer_letters.append(answer[i])

    while tries < MAX_TRIES:
        tries += 1
        guess = getInput(f"a")
        
        # Analyze guess
        for i in range(5):
            if answer[i] == guess[i]:
                print(YES, end = '')
            elif guess[i] in answer_letters:
                print(IN, end = '')
            else:
                print(NO, end = '')
        print()

        if guess == answer:
            print(f'You got it, the word was {answer.capitalize()}')
            return()
        elif tries >= 6:
            print(f'Sorry, the word was {answer.capitalize()}')
            return()

def getInput(message):
    guess = input(message)
    while guess not in guesses_list:
        guess = input(message)
    return guess
    
def readFile(filename):
    output_list = []
    file_handle = open(filename, 'r')
    for line in file_handle:
        line = line.strip()
        output_list.append(line)
    file_handle.close()
    return output_list

if __name__ == "__main__":
    # Initialization of both word lists, possible guesses and allowed answers
    # Thank you to cfreshman on github for providing well organized data for me to use :)
   
    guesses_list = readFile(GUESSES)
    answers_list = readFile(ANSWERS)

    guesses_list += answers_list

    game()
    new_game = input("Play new game? (y/n): ")
    while new_game.lower() == 'y':
        game()
        new_game = input("Play new game? (y/n): ")
