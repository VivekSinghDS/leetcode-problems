class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dfs(length):
            if length == high:
                return 1
            
            elif length > high:
                return 0 
            
            count = 1 if length >= low else 0
            count += dfs(length + zero) % mod
            count += dfs(length + one) % mod
            return count % mod
        return dfs(0) % mod
        