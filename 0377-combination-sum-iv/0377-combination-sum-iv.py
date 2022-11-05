class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def backtrack(remain):
            if remain == 0:
                return True 
            
            if remain < 0:
                return False 
            
            ans = 0
            for n in nums:
                ans += backtrack(remain - n)
                
            return ans
        return backtrack(target)
        