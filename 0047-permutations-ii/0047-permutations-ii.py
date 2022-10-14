class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(counter, cur_comb):
            nonlocal res
            if len(cur_comb) == len(nums):
                res.append(cur_comb[:])
                return 
            
            for key in counter:
                if counter[key] > 0:
                    cur_comb.append(key)
                    counter[key] -= 1
                    
                    backtrack(counter, cur_comb)
                    
                    cur_comb.pop()
                    counter[key] += 1
            
        backtrack(Counter(nums), [])
        return res
                
        