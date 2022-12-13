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
        '''
        seen = set()
        m = len(matrix)
        n = len(matrix[0])
        res = float('inf')
        
        @lru_cache(None)
        def dfs(r, c, running_sum):
            nonlocal res
            if (r, c) not in seen:
                if r == m - 1 :
                    res = min(res, running_sum)
                    running_sum -= matrix[r][c]
                    return 0
                    
                else:
                    seen.add((r, c))

                    paths = [
                            (r + 1, c), 
                            (r + 1, c + 1), 
                            (r + 1, c - 1)
                            ]
                    total = running_sum
                    for row, col in paths:
                        if (0 <= row < m and 0 <= col < n 
                            and (row, col) not in seen):
                            total += dfs(row, col, matrix[row][col] + running_sum)

                    seen.remove((r, c))

                    return total

        for i in range(m):
            # seen = set()
            dfs(0, i, matrix[0][i])
            # print('-'*10)
            
        return res
        '''
        
            
                    
                    
        