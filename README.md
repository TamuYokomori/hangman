# hangman

import random


def hangman():
    word_list = ["practice", "university", "student", "professor", "researcher"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
              "________     ",
              "|            ",
              "|       |    ",
              "|       O    ",
              "|      /|\   ",
              "|      / \   ",
              "|            ",
              ]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("WELCOME TO HANGMAN!!")
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
            print((" ".join(letter_board)))
            print("\n".join(stages[0: wrong_guesses + 1]))
        if "_" not in letter_board:
            print("YOU'RE WINNER! The word was:")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
        print("YOU'RE LOSER!! The words was {}.".format(word))

hangman()

