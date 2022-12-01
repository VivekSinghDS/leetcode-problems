class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n % 2 == 0:
                res.append(n)
                
        for n in nums:
            if n % 2 == 1:
                res.append(n)
                
        return res
            
        