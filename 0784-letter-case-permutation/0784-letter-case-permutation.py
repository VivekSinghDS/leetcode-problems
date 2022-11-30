class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def backtrack(cur_comb, index):
            nonlocal res
            if index == len(s):
                if len(cur_comb) == len(s):
                    res.append("".join(cur_comb[:]))
                return 
            
            for i in range(index, len(s)):
                if s[i].isdigit():
                    backtrack(cur_comb + [s[i]], i + 1)
                    
                else:
                    if s[i].upper() == s[i]:
                        backtrack(cur_comb + [s[i]], i + 1)
                        backtrack(cur_comb + [s[i].lower()], i + 1)
                        
                    else:
                        backtrack(cur_comb + [s[i].upper()], i + 1)
                        backtrack(cur_comb + [s[i]], i + 1)
                        
                    
        backtrack([], 0)
        return res
        