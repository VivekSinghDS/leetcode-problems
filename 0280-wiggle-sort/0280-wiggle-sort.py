class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        def swap(a, b):
            return b, a
        
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = swap(nums[i], nums[i + 1])
        return nums
        