class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nr, nc = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dp(i, j):
            if i == nr or j == nc or j < 0:
                return math.inf
            if i == nr - 1:
                return matrix[i][j]
            return matrix[i][j] + min(
                dp(i + 1, j - 1), 
                dp(i + 1, j),
                dp(i + 1, j + 1)
                      
            )
        
        return min(dp(0, j) for j in range(len(matrix[0])))