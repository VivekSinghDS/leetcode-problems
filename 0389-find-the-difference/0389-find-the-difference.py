class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        for key in t_counter:
            if key not in s_counter:
                return key
            
            elif t_counter[key] - 1 == s_counter[key]:
                return key
            
            
        
            
        