class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        res = float('inf')
        coins.sort(reverse = True)
        
        @lru_cache(maxsize = None)
        def backtrack(cur_length, remain):
            nonlocal res
            if remain < 0 or cur_length > res:
                return 
            
            if remain == 0:
                res = min(res, cur_length)
                return 
            
            for c in coins:
                remain -= c 
                cur_length += 1
                
                backtrack(cur_length, remain)
                
                remain += c
                cur_length -= 1
                
        backtrack(0, amount)
        return res if res != float('inf') else -1
        '''
        @lru_cache(None)
        def dfs(rem):
            if rem == 0:
                return 0
            
            if rem < 0:
                return -1
            
            min_cost = float('inf')
            for c in coins:
                res = dfs(rem - c)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
                    
            return min_cost if min_cost != float('inf') else -1
        
        return dfs(amount)
        
        
                
        
            
            
            
            
        