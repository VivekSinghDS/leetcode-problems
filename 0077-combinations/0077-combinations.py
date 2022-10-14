class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(index, comb):
            nonlocal res
            if len(comb) == k:
                res.append(comb[:])
                return 
            
            for i in range(index + 1, n + 1):
                backtrack(i, comb + [i])
                
        backtrack(0, [])
        return res
                
        