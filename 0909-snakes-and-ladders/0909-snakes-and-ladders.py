class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        coord = {}
        n = len(board)
        for i in range(n * n):
            # print('for i ', i)
            if (i // n) % 2 == 0:
                y = n - (i // n) - 1 
                x = (i % n)
                # print(x, y, board[y][x], ' x and y')
                coord[i + 1] = board[y][x]
                
            else:
                # print(- (i // n) - 1, n - (i % n) - 1, board[- (i // n) - 1][n - (i % n) - 1], ' x and y and board[y][x]')
                coord[i + 1] = board[ - (i // n) - 1][n - (i % n) - 1] # - (1 // 6) - 1 = -1, 4
            # print('-'*10)
        res = float('inf')
        
        min_step = float('inf')
        moves = [min_step] * (n*n +1)
        moves[1] = 0
        
        
        def dfs(curr):
            for nei in range(curr+1, min(curr+7, n*n+1)):
                if coord[nei] != -1: nei = coord[nei] # change the landing spot to snake or ladder
                if moves[curr]  + 1 < moves[nei]:
                    moves[nei] = moves[curr]+1
                    dfs(nei)
        dfs(1)
        return -1 if moves[n*n] == min_step else moves[n*n]
        # print(coordinate)
            
            
            
            
        