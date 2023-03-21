class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count_zeros = 0
        ans = 0
        l = 0
        window = {}
        for r in range(len(nums)):
            window[nums[r]] = 1 + window.get(nums[r], 0)
            
            while len(window) > 1 and l < r:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    window.pop(nums[l])
                l += 1
            
            if 0 in window:
                length = r - l + 1
                # print(window)
                ans += length
                
            
            
        return ans
        