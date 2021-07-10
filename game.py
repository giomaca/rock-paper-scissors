import random
from tkinter import *


def play(COM, PLAYER):
    if COM == PLAYER:
        wonlose["text"] = "Draw!"
    elif COM == "rock" and PLAYER == "paper" or COM == "paper" and PLAYER == "scissors" or COM == "scissors" and PLAYER == "rock":
        global playerScore
        playerScore += 1
        wonlose["text"] = "You Won!"
    else:
        global comScore
        comScore += 1
        wonlose["text"] = "You Lose!"


def comGen():
    game = ["rock", "paper", "scissors"]
    com = random.choice(game)
    return com


def rock():
    player = "rock"
    play(comGen(), player)
    score["text"] = "PLAYER {} : {} COM".format(playerScore, comScore)


def paper():
    player = "paper"
    play(comGen(), player)
    score["text"] = "PLAYER {} : {} COM".format(playerScore, comScore)


def scissors():
    player = "scissors"
    play(comGen(), player)
    score["text"] = "PLAYER {} : {} COM".format(playerScore, comScore)


playerScore = 0
comScore = 0

root = Tk()
root.title("Rock, Paper, Scissors")

#  import pictures
rockPic = PhotoImage(file="rock.png")
paperPic = PhotoImage(file="paper.png")
scissorsPic = PhotoImage(file="scissors.png")
rockPic, paperPic, scissorsPic = rockPic.subsample(5), paperPic.subsample(5), scissorsPic.subsample(5)
#  Buttons
rockButton = Button(root, text="Rock",
                    font=("Arial", 25, 'bold'),
                    image=rockPic,
                    compound=TOP,
                    width=500,
                    command=rock)
paperButton = Button(root, text="Paper",
                     font=("Arial", 25, 'bold'),
                     image=paperPic,
                     compound=TOP,
                     width=500,
                     command=paper)
scissorsButton = Button(root, text="Scissors",
                        font=("Arial", 25, 'bold'),
                        image=scissorsPic,
                        compound=TOP,
                        width=500,
                        command=scissors)

score = Label(text="PLAYER 0 : 0 COM",
              font=("Arial", 25, 'bold'))
wonlose = Label(text="",
                font=("Arial", 25, 'bold'))

wonlose.pack()
rockButton.pack()
paperButton.pack()
scissorsButton.pack()
score.pack(side=LEFT)

root.mainloop()
