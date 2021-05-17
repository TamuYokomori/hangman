# Let's program HANGMAN game.

import random


def hangman():
    word_list = ["practice", "university", "student", "professor", "researcher"]
    """ランダムでインデックス値を提示"""
    random_number = random.randint(0, 4)
    """インデックス値を使ってword_listの中の文字列をwordに渡す"""
    word = word_list[random_number]
    wrong_guesses = 0
    """最初の1行は最初から出力される([0]であるため)"""
    stages = ["",
              "________     ",
              "|            ",
              "|       |    ",
              "|       O    ",
              "|      /|\   ",
              "|      / \   ",
              "|            ",
              ]
    """文字列を一文字ずつの文字列のリストに分解"""
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    """初期状態ではfalseを割り当て、勝ったかどうかの状態を記録"""
    win = False
    print("WELCOME TO HANGMAN!!")
    """最後の間違いを入力して解析したらwhileは止まる。wrongは0回〜、stageの長さは1〜8まである"""
    """帳尻合わせでstageから1を引く"""
    """wrong=stageはelse文の中で成立"""
    while wrong_guesses < len(stages) - 1:
        """ただ見た目として1行空ける"""
        print("\n")
        guess = input("Guess a letter: ")
        """答えの中に入力文字が入っている場合"""
        if guess in remaining_letters:
            """入力文字のインデックス値を引き出す"""
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            """そのインデックス値の文字列を$と定義することで次に他の重複文字のインデックス値を返せる"""
            remaining_letters[character_index] = '$'
        """間違った文字を入れた場合"""
        else:
            wrong_guesses += 1
        """半角スペースで文字列を連結したものを返す"""
            print((" ".join(letter_board)))
        """指定範囲の文字列を改行で連結して返す。終インデックス値は含まれないからwrong+1"""
            print("\n".join(stages[0: wrong_guesses + 1]))
        """文字が全て埋まり_がない状態の時"""
        if "_" not in letter_board:
            print("YOU'RE WINNER! The word was:")
            """埋まったリストのオブジェクトを全て連結させて答えを出力"""
            print(" ".join(letter_board))
            """状態を変換"""
            win = True
            break
    """Falseつまりwhile関数が否定された場合"""
    if not win:
        print("YOU'RE LOSER!! The words was {}.".format(word))

hangman()
