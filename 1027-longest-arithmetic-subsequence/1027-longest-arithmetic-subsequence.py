class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
        res = 1
        
        dp = {}
        def solve(i, diff):
            if (i, diff) in dp:
                return dp[(i, diff)]
            if i < 0:
                return 0
            
            ans = 0
            for j in range(i - 1, -1, -1):
                if nums[i] - nums[j] == diff:
                    ans = max(ans, 1 + solve(j, diff))
            
            dp[(i, diff)] = ans
            return ans
                
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                res = max(res, 2 + solve(i, diff))
                
        return res
        
        '''
        mapper = {}
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                mapper[j, nums[j] - nums[i]] = mapper.get((i, nums[j] - nums[i]), 1) + 1
                
        return max(mapper.values())
            
        