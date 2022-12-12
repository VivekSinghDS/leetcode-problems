class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        res = 0
        for key in counter:
            if counter[key] == 1:
                return -1
            
            if counter[key] % 3 == 0:
                res += (counter[key] // 3)
                
            else:
                res += (counter[key] // 3) + 1
                
        return res
            
        
                    
                
                
        