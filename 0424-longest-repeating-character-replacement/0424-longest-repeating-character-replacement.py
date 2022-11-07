class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        window = {}
        ans = 0
        max_val = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            max_val = max(max_val, window[s[r]])
                
            
            while r - l + 1 - max_val > k:
                window[s[l]] -= 1
                l += 1
                
                
            ans = max(ans, r - l + 1)
        return ans
                
                
        