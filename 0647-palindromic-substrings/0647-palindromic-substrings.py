class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def efc(left, right):
            length = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                length += 1
                
            return length 
        
        res = 0
        for i in range(len(s)):
            res += efc(i, i) + efc(i, i + 1)
            
        return res
            
                
        