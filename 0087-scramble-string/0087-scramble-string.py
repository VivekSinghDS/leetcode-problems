class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @cache
        def dfs(s1, s2):
            if len(s1) == 1 or (s1 == s2):
                return s1 == s2
            
            size = len(s1)
            for i in range(1, size):
                if ((dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:])) or 
                    (dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]))):
                    
                    return True
                    
            return False
        
        return dfs(s1, s2)
                    
                    
                    
            
                
                
            
            
            
        