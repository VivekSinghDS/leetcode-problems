class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        length = len(palindrome)
        if length == 1:
            return ""
        for i in range(int(length/2)):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        
        palindrome = palindrome[:length - 1] + "b"
        return palindrome

    
        
            
        
        