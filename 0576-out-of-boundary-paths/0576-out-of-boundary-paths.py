class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def backtrack(r, c, moves):
            # print(r, c, moves)
            if moves == 0 and (r < 0 or c < 0 or r == m or c == n):
                return 1
            
            elif moves == 0 and (0 <= r < m and 0 <= c < n):
                return 0
            
            elif moves > 0 and (r < 0 or c < 0 or r == m or c == n):
                return 1 
            
            paths = [(r + 1, c), 
                    (r - 1, c), 
                    (r, c + 1), 
                    (r, c - 1)]
            
            total = 0
            for row, col in paths:
                total += backtrack(row, col, moves - 1)
               
            return total % (10 ** 9 + 7)
        
        return backtrack(startRow, startColumn, maxMove)
        
        