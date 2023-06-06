class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference = None
        
        for i in range(1, len(arr)):
            if difference is None:
                difference = arr[i] - arr[i - 1]
                
            else:
                new = arr[i] - arr[i - 1]
                if difference != new:
                    return False
                
        return True
            
            
        