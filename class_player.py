class Player():
    def __init__(self, board):
        self.board = board

    def movement(self, row, col):
        if self.board.board[row][col] == " ":
            self.board.board[row][col] = self.board.currentPlayer
            return True
        else:
            return False
    
    def changeTurn(self):
        self.board.currentPlayer = "O" if self.board.currentPlayer == "X" else "X"