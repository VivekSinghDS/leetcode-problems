class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = i3 = i5 = 0
        nums = [1,]
        for i in range(1, n + 1):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)
            
            if ugly == nums[i2] * 2:
                i2 += 1
                
            if ugly == nums[i3] * 3:
                i3 += 1
                
            if ugly == nums[i5] * 5:
                i5 += 1
                
        return nums[n - 1]
        