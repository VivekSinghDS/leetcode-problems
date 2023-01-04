class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        
        @cache
        def coinchange(n):
            if n == 1:
                return float('inf')
            
            elif n == 2 or n == 3:
                return 1
            
            ans = float('inf')
            if n >= 2:
                ans = min(ans, 1 + coinchange(n - 2))
                
            if n >= 3:
                ans = min(ans, 1 + coinchange(n - 3))
                
                
            return ans
        
        res = 0
        for values in counter.values():
            ways = coinchange(values)
            if ways == float('inf'):
                return -1
            # print(ways)
            res += ways 
            
        return res
                
            
        