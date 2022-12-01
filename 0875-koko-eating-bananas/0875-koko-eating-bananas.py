class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        
        while left < right:
            
            middle = (left + right) // 2
            # print(left, right, middle)
            hour_spent = 0
            
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
                
            if hour_spent <= h:
                right = middle
                
            else:
                left = middle + 1
                
        # print(left, right)
        return right
                
        
                
            
            
        