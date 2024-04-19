import class_board as cboard
import class_player as cplayer

class Hashtag:
    def __init__(self):
        self.board = cboard.Board()
        self.player = cplayer.Player(self.board)

    def play(self):
        while True:
            self.board.printBoard()
            row = int(input("Enter row number (0, 1, 2): "))
            col = int(input("Enter column number (0, 1, 2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            if self.player.movement(row, col):
                if self.board.whoWin():
                    self.board.printBoard()
                    print(f"Player {self.board.currentPlayer} wins!")
                    break
                elif self.board.isFull():
                    self.board.printBoard()
                    print("It's a tie!")
                    break
                else:
                    self.player.changeTurn()
            else:
                print("That cell is already taken. Try again.")
    