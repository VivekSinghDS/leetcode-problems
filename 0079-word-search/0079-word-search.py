class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        
        
        def dfs(r, c, index):
            if index == len(word):
                return True 
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]
                or (r, c) in visited):
                return False
            
            visited.add((r, c))
            
            
            paths = [(r + 1, c), 
                    (r - 1, c),
                    (r, c + 1), 
                    (r, c - 1)]
            
            ans = False
            for row, col in paths:
                ans |= dfs(row, col, index + 1)
                
            visited.remove((r, c))
                
            return ans 
        
        for r in range(rows):
            for c in range(cols):
                visited = set()
                if dfs(r, c, 0):
                    return True
                    
        return False
                
            
            
            
        