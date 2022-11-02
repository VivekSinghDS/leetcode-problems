class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n + 1)
        dp[0] = 0
        
        squares = [i ** 2 for i in range(n + 1) if i**2 <= n]
        for target in range(1, n + 1):
            for square in squares:
                # square = s ** 2 
                
                if target - square < 0:
                    break 
                
                if 1 + dp[target - square] < dp[target]:
                    dp[target] = 1 + dp[target - square]
                
    
        return(dp[n])
    
'''
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        numbers = []
        for i in range(1, int(n ** 0.5) + 1):
            
            if i ** 2 <= n:
                numbers.append(i * i)
        
        
        comb = []
        res = float('inf')
        
        @lru_cache(maxsize = None)
        def backtrack_reverse(remain, comb):
            nonlocal res
            if remain == 0:
                # print(comb)
                res = min(res, len(comb))
                return 
            
            elif remain < 0 or len(comb) > res:
                return  
            
            
            comb = list(comb)
            for number in numbers[::-1]:
                backtrack_reverse(remain - number, tuple(comb + [number]))
                
        backtrack_reverse(n, tuple(comb))
        return res

'''
        
        
                
        