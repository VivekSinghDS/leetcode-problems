class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        res = []
        
        def backtrack(cur_comb):
            if len(cur_comb) == n:
                res.append(int("".join(cur_comb[:])))
                return 
            
            for i in range(10):
                if not cur_comb and i == 0:
                    continue 
                    
                elif not cur_comb:
                    backtrack(cur_comb + [str(i)])
                    
                else:
                    if abs(int(cur_comb[-1]) - i) == k:
                        backtrack(cur_comb + [str(i)])
                    
        backtrack([])
        return res
                