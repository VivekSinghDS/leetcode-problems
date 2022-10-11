class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        n = len(needle)
        l = 0 
        window = haystack[:n]
        if window == needle:
            return 0 
        

        for r in range(len(needle), len(haystack)):
            window += haystack[r] 
            l += 1
            window = window[1:]
            
            if window == needle:
                return l
            

        return -1
                
            
                
            
        