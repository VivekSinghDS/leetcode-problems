class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        l = 0
        s2_counter = {}
        l1 = len(s1)
        for r in range(len(s2)):
            s2_counter[s2[r]] = 1 + s2_counter.get(s2[r], 0)
            
            while r - l + 1 > l1:
                s2_counter[s2[l]] -= 1
                if s2_counter[s2[l]] == 0:
                    s2_counter.pop(s2[l])
                l += 1
                
            if r - l + 1 == l1:
                if s1_counter == s2_counter:
                    return True 
                
        return False
        
        