class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize = None )
        def climb(x):
            if x < 0:
                return 0 
            
            elif x == 0:
                return 1
            
            total = climb(x - 1) + climb(x - 2)
            return total
        
        return climb(n)