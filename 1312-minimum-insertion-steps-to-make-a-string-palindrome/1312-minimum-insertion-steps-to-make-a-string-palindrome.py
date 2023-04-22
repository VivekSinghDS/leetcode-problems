class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        @cache
        def dfs(left, right):
            best = float('inf')
            if left >= right:
                return 0
            
            if s[left] == s[right]:
                best = min(best, dfs(left + 1, right - 1))
                
            best = min(best, 1 + dfs(left + 1, right), 1 + dfs(left, right - 1))
            return best
            
        
        return dfs(0, len(s) - 1)
        
            
        