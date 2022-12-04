class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sum_uptil_now = []
        running_sum = 0
        
        total = sum(nums)
            
        # print(sum_uptil_now)
        length = len(nums)
        res = float('inf')
        result = None
        for i in range(length):
            running_sum += nums[i]
            # print(i + 1, length - i - 1, res)
            cur_length = i + 1
            first = int(running_sum / cur_length)
            if i == (length) - 1:
                second = 0
                
            else:
                second = int((total - running_sum) / (length - i - 1))
            # print(first, second)
            ans = abs(first - second)
            
            if ans < res:
                result = i
                res = ans
                
            # print('-'*10)
                
            
            
        return result
            
            
            
        