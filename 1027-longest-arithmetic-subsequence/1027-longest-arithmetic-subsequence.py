class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        mapper = defaultdict(int)
        
        for right in range(len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]
                mapper[(right, difference)] = max(mapper[(right, difference)], 1 + mapper[(left, difference)])
        return max(mapper.values()) + 1
        