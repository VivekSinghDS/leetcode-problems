class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0 
        
        for right_end in range(len(nums) - 1, -1, -1):
            # print(nums[right_end], nums[right_end - 1])
            if nums[right_end] > nums[right_end - 1]:
                pivot = right_end 
                break 
        
        if not pivot:
            nums.sort()
            return 
        
        swap = len(nums) - 1
        
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1
            
        nums[pivot - 1], nums[swap] = nums[swap], nums[pivot - 1]
        nums[pivot:] = nums[pivot:][::-1]

        