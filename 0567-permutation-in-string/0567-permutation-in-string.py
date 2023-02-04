class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = {}
        
        l = 0 
        
        for r in range(len(s2)):
            c2[s2[r]] = 1 + c2.get(s2[r], 0)
            
            while r - l + 1 > len(s1):
                c2[s2[l]] -= 1
                
                if c2[s2[l]] == 0:
                    c2.pop(s2[l])
                    
                l += 1
                
            if c1 == c2:
                return True 
            
        return False