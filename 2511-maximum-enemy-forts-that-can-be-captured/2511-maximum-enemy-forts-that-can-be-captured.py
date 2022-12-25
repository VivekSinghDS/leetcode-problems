class Solution:
    def captureForts(self, forts: List[int]) -> int:
        stack = []
        ans = 0
        for i, value in enumerate(forts):
            
            if stack and forts[stack[-1]] == -1*value:
                ans = max(ans, i - stack[-1] -1)
                stack.append(i)
                
            if value == 1 or value == -1:
                stack.append(i)
                
            # print(stack, ans)
                

                
        return ans
        