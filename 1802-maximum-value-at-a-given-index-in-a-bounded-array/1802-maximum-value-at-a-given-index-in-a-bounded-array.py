class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def getSum(index, middle, n):
            count = 0
            if middle > index:
                count += (middle + middle - index) * (index + 1) // 2
            else:
                count += middle * (middle + 1) // 2 + index - middle + 1
                
            if middle >= n - index:
                count += (middle + middle - n + 1 + index) * (n - index) // 2
            else:
                count += (middle + 1) * middle // 2 + n - index - middle
        
            return count - middle

        
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left
        