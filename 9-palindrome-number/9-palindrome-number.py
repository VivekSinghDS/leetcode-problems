class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x * -1 > 0:
            return False
        y = x 

        res = 0 
        
        while y:
            digit = int(math.fmod(y, 10))
            y = int(y / 10)
            
            res = (res*10) + digit
            
        return(res == x)
        