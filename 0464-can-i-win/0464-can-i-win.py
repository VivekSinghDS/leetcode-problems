class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def has_used(flag, x):
            return flag & (1 << x)
        
        def is_odd(n):
            return n % 2 == 1
        
        total = maxChoosableInteger * (maxChoosableInteger + 1)/2
        if total < desiredTotal:
            return False
        
        elif total == desiredTotal and is_odd(maxChoosableInteger):
            return True 
        
        elif desiredTotal <= 0:
            return True
            
        @cache
        def dfs(remain, bitflag):
            if remain <= 0:
                return False
            
            for number in range(1, maxChoosableInteger + 1):
                if has_used(bitflag, number):
                    continue 
                    
                if not dfs(remain - number, bitflag | (1 << number)):
                    return True 
                
            return False
        
        return dfs(desiredTotal, 0)
        
        
        