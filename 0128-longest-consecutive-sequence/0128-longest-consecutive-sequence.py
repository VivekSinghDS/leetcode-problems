class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        
        for n in nums:
            if n - 1 not in nums:
                count = 0
                while n + count in nums:
                    count += 1
                    
                ans = max(ans, count)
                    
        return ans 
        