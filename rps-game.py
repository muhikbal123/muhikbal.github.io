from random import randint

# variable
choice = ['rook', 'paper', 'scissor']
# user computer
computer = choice[randint(0,2)]
# set variabel player = false
player = False

while player == False :
    # enter player selection
    player = input("rook, paper, scissor = ")
    if computer == player :
        print("computer select = ", computer)
        print("draw game!!")
    elif player == 'rook':
        if computer == 'paper' :
            print("computer select paper")
            print("you lose!!!")
        else :
            print("computer select scissor")
            print("you win!!!")
    elif player == 'paper':
        if computer == 'scissor' :
            print("computer select scissor")
            print("you lose!!!")
        else :
            print("computer select rook")
            print("you win!!!")
    elif player == 'scissor':
        if computer == 'rook' :
            print("computer select rook")
            print("you lose!!!")
        else :
            print("computer selected papper")
            print("you win!!!")
    else:
        print("you choise wrong!!!, please reselect!!!")
    player = False
    computer = choice[randint(0,2)]
