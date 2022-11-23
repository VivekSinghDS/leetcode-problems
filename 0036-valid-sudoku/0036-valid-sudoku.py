class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board[0]))]
        boxes = [set() for i in range(len(board))]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue 
                    
                value = board[r][c]
                if value in rows[r]:
                    return False
                
                rows[r].add(value)
                if value in cols[c]:
                    return False
                cols[c].add(value)
                
                idx = (r // 3) * 3 + c // 3
                if value in boxes[idx]:
                    return False
                
                boxes[idx].add(value)
                
        return True
        