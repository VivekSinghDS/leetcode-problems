class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        bitwise = 0
        
        for ch in s:
            bitwise ^= ord(ch)
            
        for ch in t:
            bitwise ^= ord(ch)
            
        return chr(bitwise)
            
            
        
            
        