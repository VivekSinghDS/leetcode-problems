class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dfs(index, k):
            if index == len(piles):
                return 0 
            
            res = dfs(index + 1, k)
            score = 0
            
            for j in range(min(k, len(piles[index]))):
                score += piles[index][j]
                include = score + dfs(index + 1, k - j - 1)
                
                res = max(res, include)
                
            return res
        
        return dfs(0, k)
                
                
        