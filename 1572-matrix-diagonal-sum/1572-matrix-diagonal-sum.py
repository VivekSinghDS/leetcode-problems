class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        def calculate(mat):
            total = 0
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if ((i == j)):
                        # print(i, j)
                        total += mat[i][j]

            return total
        
        ans = calculate(mat)
        n = len(mat)
        mat = [x[::-1] for x in mat]
        ans += calculate(mat)
        
        if len(mat) % 2 == 1:
            ans -= mat[n // 2][n // 2]
            
        return ans
        
        
        
            
        