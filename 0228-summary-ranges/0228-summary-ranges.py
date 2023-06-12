class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        stack = []
        res = []
        for i in range(len(nums)):
            if stack and stack[-1] + 1 == nums[i]:
                if len(stack) > 1:
                    stack.pop()
                stack.append(nums[i])
                
            else:
                res.append(stack)
                stack = [nums[i]]
        if stack:
            res.append(stack)
        ans = []
        
        for val in res:
            if len(val) == 0:
                continue 
            elif len(val) == 1:
                ans.append(str(val[0]))
            else:
                ans.append(str(val[0]) + "->" + str(val[1]))
        return ans
                