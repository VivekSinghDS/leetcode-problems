class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])
        l = 0 
        res = []
        if p_counter == s_counter:
            res.append(0)
            
        for r in range(len(p), len(s)):
            s_counter[s[r]] = 1 + s_counter.get(s[r], 0)
            
            while r - l + 1 > len(p):
                s_counter[s[l]] -= 1
                l += 1
                
                if s_counter[s[l]] == 0:
                    s_counter.pop(s[l])
                    
            if p_counter == s_counter:
                res.append(l)
                
        return res
                
        