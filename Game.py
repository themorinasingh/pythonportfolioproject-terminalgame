print("Welcome to Tic Tac Tow")

class Board:
    def __init__(self):
        self.board_design = [" ", " "," "," "," "," "," "," "," "," "]

    def board_display(self):
        print(" {} | {} | {} ".format(self.board_design[1],self.board_design[2],self.board_design[3]))
        print("-----------")
        print(" {} | {} | {} ".format(self.board_design[4],self.board_design[5],self.board_design[6]))
        print("-----------")
        print(" {} | {} | {} \n".format(self.board_design[7],self.board_design[8],self.board_design[9]))

    def move(self,player):
        pass
        



board1 = Board()

board1.board_display()

class Player :
    def __init__(self, name) :
        self.name = name
        self.char = ""

player1_name = input("Player 1, Enter Your Name: \n").title()
player_1 = Player(player1_name)

player2_name = input("Player 2, Enter Your Name: \n").title()
player_2 = Player(player2_name)

player_1.char = input("{} Do you choose X or O: \n".format(player_1.name)).upper()

if player_1.char == "X" :
    player_2.char = "O"
elif player_1.char == "O":
    player_2.char = "O"

print("{} you have been assigned {}".format(player_2.name, player_2.char))

print("Let's start the game!\n")