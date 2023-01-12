class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache 
        def dfs(current):
            # print(current)
            if current == 0:
                return 1
            
            if current < 0:
                return 0
            
            return dfs(current - 1) + dfs(current - 2)
        
        return dfs(n)
        