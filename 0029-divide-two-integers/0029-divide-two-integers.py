class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d, di = abs(dividend), abs(divisor)
        output = 0
        while d >= di:
            temp = di
            mul = 1
            
            while d >= temp:
                d -= temp 
                output += mul
                mul += mul
                temp += temp
                
        if((dividend < 0 and divisor >0) or (dividend>0 and divisor < 0)):
            output = -1*output
        
        return min(2147483647, max(output, -2147483648))
        