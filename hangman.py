
def hangman(word):
    wrong=0
    stages=["",
            "________________              ",
            "|              |              ",
            "|              |              ",
            "|              0              ",
            "|             /|\             ",
            "|             / \             ",
            "|                             "
            ]
    rletter=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ！！")

    while wrong<len(stages)-1:
        print("\n")
        msg="アルファベット1文字入力してね？"
        char=input(msg)
        if char in rletter:
            cind=rletter.index(char)
            board[cind]=char
            rletter[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ちです！！")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

hangman("cat")
        
    
            
