class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = self.antidiagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1
        
        self.rows[row] += current_player
        self.cols[col] += current_player 
        
        if row == col:
            self.diagonal += current_player
            
        if col == len(self.cols) - row - 1:
            self.antidiagonal += current_player
        
        n = len(self.rows)
        if n in [abs(self.rows[row]), abs(self.cols[col]), abs(self.diagonal), abs(self.antidiagonal)]:
            return player 
        return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)