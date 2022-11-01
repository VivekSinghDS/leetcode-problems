class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        one_odd = False 
        
        counter = Counter(s)
        
        for key in counter:
            if counter[key] % 2 == 1:
                if one_odd == True:
                    return False 
                
                one_odd = True 
                
        return True
        