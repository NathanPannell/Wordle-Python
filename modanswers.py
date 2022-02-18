if __name__ == "__main__":
    '''
    Adding answers.txt to guesses.txt means that guesses.txt includes EVERY word instead of just the uncommon ones
    '''
    answers = open("answers.txt", "r")
    guesses = open("guesses.txt", "a")

    # Need to add a newline character before appending because words go right to the end and there is no \n to start appending to
    guesses.write("\n")
    for line in answers:
        guesses.write(line)
    answers.close()
    guesses.close()