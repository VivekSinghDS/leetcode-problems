class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum_of_minimums = 0
        stack = []
        MOD = 10 ** 9 + 7
        
        for i in range(len(arr) + 1):
            
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                
                count = (mid - left) * (right - mid)
                sum_of_minimums += arr[mid] * count
                
            stack.append(i)
                
        return sum_of_minimums % MOD
        