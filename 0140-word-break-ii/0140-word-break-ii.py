class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        
        @cache
        def backtrack(cur_comb, string):
            nonlocal res
            cur_comb = list(cur_comb)
            if len(string) == 0:
                res.append(" ".join(cur_comb))
                return 
            
            for word in wordDict:
                if string[:len(word)] == word:
                    backtrack(tuple(cur_comb + [word]), string[len(word):])
                    
        backtrack(tuple([]), s)
        return res
                    
            
                
                