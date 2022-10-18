class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        if len(word) > rows * cols:
            return False
        seen = set()
        def dfs(r, c, i):
            if i == len(word):
                return True 
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i] or (r, c) in seen):
                return False 
            
            seen.add((r, c))
            ans = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or\
                  dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            
            seen.remove((r, c))
            return ans 
        
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c] and dfs(r, c, 0):
                    return True
                
        return False
            
        