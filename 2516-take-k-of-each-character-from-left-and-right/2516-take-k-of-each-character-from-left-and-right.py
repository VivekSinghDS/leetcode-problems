class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        for key in ['a', 'b', 'c']:
            if counter[key] - k < 0:
                
                return -1
            else:
                counter[key] -= k
                
        
        l = 0 
        window = defaultdict(int)
        res = 0
        for r in range(len(s)):
            window[s[r]] += 1
            
            while window[s[r]] > counter[s[r]]:
                window[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        
        
        return len(s) - res
                
            
            
        