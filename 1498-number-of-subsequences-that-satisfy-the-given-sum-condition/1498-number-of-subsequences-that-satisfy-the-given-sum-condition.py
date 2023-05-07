class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        nums.sort()
        res = 0
        for left in range(len(nums)):
            right = bisect_right(nums, target - nums[left]) - 1
            
            if left <= right:
                res += 2**(right - left) % mod
        return res % mod