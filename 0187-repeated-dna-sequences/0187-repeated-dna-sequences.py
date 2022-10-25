class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        l = 0 
        res = []
        window = ""
        hash_set = set()
        for r in range(len(s)):
            window += s[r]
            if not(r - l + 1 >= 10):
                continue 
                
            if window in hash_set:
                res.append(window)
                
            else:
                hash_set.add(window)
                
            window = window[1:]
            
        return list(set(res))
                
            
                
            
                
            
                
                
                
            
        