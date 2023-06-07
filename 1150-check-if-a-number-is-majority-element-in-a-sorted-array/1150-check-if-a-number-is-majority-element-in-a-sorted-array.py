class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        first = bisect_left(nums, target)
        last = bisect_right(nums, target)
        
        return True if last - first > len(nums) / 2 else False
        # print(first, last)
            