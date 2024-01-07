import random
def ggg():
    word_list = ["red","orange","cat","laptop","mouse", "notepad"]
    word = random.choice(word_list)
    print(word)
    return word

def hangman():
    word = ggg()
    wrong = 0
    stages = ["",
              "________     ",
              "|        ",
              "|    |   ",
              "|    6   ",
              "|   /|\   ",
              "|   / \   ",
              "|      ",
              "|        "
              ]
    #create a list of the word's letters
    rletters = list(word)
    #create a board for each letter (hidden)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        #find the letter's index, replace "__" in the board list with it; replace it with "$" in the char list of the word
        if char in rletters:
            cind = rletters.index(char)
            board[cind]=char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
hangman()
