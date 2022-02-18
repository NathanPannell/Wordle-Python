if __name__ == "__main__":
    '''
    Adding the answers.txt to guesses.txt means that guesses includes EVERY word from the start instead of just the uncommon
    '''
    answers = open("answers.txt", "r")
    guesses = open("guesses.txt", "a")

    # Need to add a newline character before appending because words go right to the end and there is no \n to start appending to
    guesses.write("\n")
    for line in answers:
        guesses.write(line)
    answers.close()
    guesses.close()