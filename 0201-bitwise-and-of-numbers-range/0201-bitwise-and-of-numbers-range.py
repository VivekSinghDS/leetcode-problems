class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        m, n = left, right
        shift = 0
        while m < n:
            m >>= 1
            n >>= 1
            
            shift += 1
            
        return m << shift
            
            
        