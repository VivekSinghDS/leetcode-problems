class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, comb):
            res.append(comb[:])
            
            for i in range(index + 1, len(nums)):
                backtrack(i, comb + [nums[i]])
                
        
        backtrack(-1, [])
        return(res)
        