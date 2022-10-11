class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(n_open, n_closed, cur_comb):
            nonlocal res
            if n_open == n_closed == n:
                res.append(cur_comb[:])
                return 
            
            if n_open < n:
                backtrack(n_open + 1, n_closed, cur_comb + "(")
                
            if n_closed < n_open:
                backtrack(n_open, n_closed + 1, cur_comb + ")")
                
        backtrack(0, 0, "")
        return res
                
        