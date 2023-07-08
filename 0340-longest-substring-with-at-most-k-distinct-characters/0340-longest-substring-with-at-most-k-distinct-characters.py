class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = defaultdict(int)
        res = 0
        l = 0
        
        for r in range(len(s)):
            window[s[r]] += 1
            
            while len(window) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    window.pop(s[l])
                l += 1
            
            res = max(res, r - l + 1)
        return res
    