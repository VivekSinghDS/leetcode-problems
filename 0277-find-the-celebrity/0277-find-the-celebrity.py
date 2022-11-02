# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def isCeleb(candidate):
            for other_candidate in range(n):
                if candidate == other_candidate:
                    continue 
                    
                if knows(candidate, other_candidate) or not(knows(other_candidate, candidate)):
                    return False 
                
            return True 
        
        celeb_candidate = 0
        
        for candidate in range(n):
            if knows(celeb_candidate, candidate):
                celeb_candidate = candidate
                
        if isCeleb(celeb_candidate):
            return celeb_candidate
        
        return -1 
        