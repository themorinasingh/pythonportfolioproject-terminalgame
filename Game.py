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
        print("{} Choose a number from 1 to 9.".format(player.name))
        number = int(input())
        player.moves.append(number)
        if player.char == "X" :
            self.board_design[number] = "X"
        elif player.char == "O" :
            self.board_design[number] = "O"

    def who_wins(self, player) :
        winning_combos = [ [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        for combo in winning_combos:
            win_counter = 0
            for number in combo :
                if number in player.moves:
                    win_counter += 1
            
            if win_counter == 3 :
                print("{} wins the game".format(player.name))



board1 = Board()

board1.board_display()

class Player :
    def __init__(self, name) :
        self.name = name
        self.char = ""
        self.moves = []

player1_name = input("Player 1, Enter Your Name: \n").title()
player_1 = Player(player1_name)

player2_name = input("Player 2, Enter Your Name: \n").title()
player_2 = Player(player2_name)

player_1.char = input("{} Do you choose X or O: \n".format(player_1.name)).upper()

if player_1.char == "X" :
    player_2.char = "O"
elif player_1.char == "O":
    player_2.char = "X"

print("{} you have been assigned {}".format(player_2.name, player_2.char))

print("Let's start the game!\n")

#running the game
moves = 0
while True :
    moves += 1
    board1.move(player_1)
    board1.board_display()

    board1.who_wins(player_1)

    if moves >= 9 :
        break

    moves += 1
    board1.move(player_2)
    board1.board_display()

    board1.who_wins(player_1)
    
    
