class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sum_uptil_now = []
        running_sum = 0
        
        for n in nums:
            running_sum += n
            sum_uptil_now.append(running_sum)
            
        # print(sum_uptil_now)
        length = len(nums)
        res = float('inf')
        result = None
        for i in range(length):
            # print(i + 1, length - i - 1, res)
            cur_length = i + 1
            first = int(sum_uptil_now[i] / cur_length)
            if i == (length) - 1:
                second = 0
                
            else:
                second = int((sum_uptil_now[-1] - sum_uptil_now[i]) / (length - i - 1))
            # print(first, second)
            ans = abs(first - second)
            
            if ans < res:
                result = i
                res = ans
                
            # print('-'*10)
                
            
            
        return result
            
            
            
        