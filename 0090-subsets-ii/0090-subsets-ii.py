class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(index, cur_comb):

            res.append(cur_comb[:])
            
            for i in range(index, len(nums)):
                if nums[i] == nums[i - 1] and i > index:
                    continue 
                    
                backtrack(i + 1, cur_comb + [nums[i]])
                
        backtrack(0, [])
        return res
                
        