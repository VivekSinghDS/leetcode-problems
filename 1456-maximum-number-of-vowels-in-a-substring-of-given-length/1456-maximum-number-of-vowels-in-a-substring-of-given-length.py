class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        l = 0 
        vowel_count = 0 
        current_string = ""
        for r in range(len(s)):
            current_string += s[r]
            if s[r] in "aeiou":
                vowel_count += 1
                
            while r - l + 1 > k and l < r:
                if s[l] in "aeiou":
                    vowel_count -= 1
                    
                l += 1
            
            res = max(res, vowel_count)
        return res
                
            
        