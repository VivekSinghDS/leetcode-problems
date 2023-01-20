class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        def backtrack(index, cur_comb):
            if len(cur_comb) > 1:
                res.append(cur_comb)
                
            if index >= len(nums):
                return 
            
            for i in range(index, len(nums)):
                if cur_comb and cur_comb[-1] <= nums[i]:
                    backtrack(i + 1, cur_comb + [nums[i]])
                    
                elif not cur_comb:
                    backtrack(i + 1, cur_comb + [nums[i]])
                    
        backtrack(0, [])
        return set([tuple(x) for x in res])
                
                
        