class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = Counter(s)
        odd_once = True 
        
        for key in counter:
            if counter[key] % 2 == 0:
                ans += counter[key]
            else:
                odd_once = False
                ans += (counter[key] - 1)
                
        return ans if odd_once else ans + 1

        