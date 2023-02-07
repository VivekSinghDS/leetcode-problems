class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        total = 0
        mapper = {}
        l = 0
        count = 0
        res = 0
        
        for r in range(len(fruits)):
            mapper[fruits[r]] = 1 + mapper.get(fruits[r], 0)
            
            
            if mapper[fruits[r]] == 1:
                total += 1
                
            while total >= 3:
                mapper[fruits[l]] -= 1
                
                if mapper[fruits[l]] == 0:
                    mapper.pop(fruits[l])
                    total -= 1
                    
                l += 1
                    
            res = max(res, r - l + 1)
        return res
                    
            
                
                
        
        