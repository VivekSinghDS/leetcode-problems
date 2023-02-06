class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #[2,5,1,3,4,7]
        
        for i in range(n, 2 * n):
            second = nums[i] << 10
            nums[i - n] |= second 
            
            
        all_ones = int(pow(2, 10)) - 1
        
        for i in range(n - 1, -1, -1):
            second = nums[i] >> 10
            first = nums[i] & all_ones
            nums[2*i + 1] = second 
            nums[2*i] = first
            
        return nums
        