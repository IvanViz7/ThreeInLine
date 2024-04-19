class Board():
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range (3)]
        self.currentPlayer = "X"
        #Printing the board for the game
    def printBoard(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
    
    #Analizing who is the winner of the game
    def whoWin(self):
        for row in self.board:
            if all(cell == self.currentPlayer for cell in row):
                return True
            
        for col in range(3):
            if all(row[col] == self.currentPlayer for row in self.board):
                return True
        
        if all(self.board[i][i] == self.currentPlayer for i in range(3)):
            return True
        if all(self.board[i][2-i] == self.currentPlayer for i in range(3)):
            return True

        return False
    
    def isFull(self):
       return all(cell != " " for row in self.board for cell in row)     
    
