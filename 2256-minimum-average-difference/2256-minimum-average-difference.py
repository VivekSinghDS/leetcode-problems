class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        running_sum = 0
        
        total = sum(nums)

        length = len(nums)
        res = float('inf')
        result = None
        for i in range(length):
            running_sum += nums[i]
            cur_length = i + 1
            first = int(running_sum / cur_length)
            if i == (length) - 1:
                second = 0
                
            else:
                second = int((total - running_sum) / (length - i - 1))

            ans = abs(first - second)
            
            if ans < res:
                result = i
                res = ans

        return result
            
            
            
        