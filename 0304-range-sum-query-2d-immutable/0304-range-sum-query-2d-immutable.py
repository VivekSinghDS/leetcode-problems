class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.mat = [[0]*(n + 1) for _ in range(m + 1)]
        
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.mat[r][c] = self.mat[r - 1][c] + self.mat[r][c - 1] - self.mat[r - 1][c - 1]+ matrix[r - 1][c - 1] 
                
                
                
        # print(self.mat)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        return (self.mat[r2][c2] - self.mat[r2][c1 - 1] - self.mat[r1 - 1][c2] + self.mat[r1 - 1][c1 - 1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)