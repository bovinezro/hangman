import random, sys

word_list = []
game = 1

while True:
    for line in open(sys.argv[1]).read().splitlines():
        word_list.append(line)

    word_to_guess = word_list[random.randint(0,len(word_list) - 1)]
    guesses = 10

    def blank_maker(word_to_guess):
        blanks = []
        length = len(word_to_guess) + 1
        location = -1

        while length > 0:
            blanks += "_"
            length -= 1

        while True:
            location = word_to_guess.find(" ", location + 1)
            blanks[location] = " "
            if location == -1:
                break
            else:
                loation = -1
                pass
        return blanks

    print(f"Game number {game}. The word has {len(word_to_guess)} letters.")
    blanks = blank_maker(word_to_guess)

    while guesses > 0:
        location = -1
        values = []

        print("".join(blanks) + f"You have {guesses} guesses remaining. Please enter one letter.")
        guess = input()

        while guess.isalpha() == False or len(guess) != 1:
            print("Invalid input. Please enter one letter.")
            guess = input()

        while True:
            location = word_to_guess.lower().find(guess, location + 1)
            values.append(location)
            if location == -1:
                break

        if len(values) == 1:
            guesses -= 1

        for i in values:
            if i != -1:
                blanks[i] = guess

        if "".join(blanks) == word_to_guess.lower()+" ":
            print(f"Congratulations, you won with {guesses} guesses left!")
            guesses = 0
        elif guesses == 0:
            print("Sorry, better luck next time!")

    print("Play again? y/n")
    replay = input()
    game += 1
    if replay.lower() != "y":
        break
