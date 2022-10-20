class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        

        def backtrack(cur_comb, string):
            nonlocal res
            if len(string) == 0:
                res.append(" ".join(cur_comb))
                return 
            
            for word in wordDict:
                if string[:len(word)] == word:
                    backtrack(cur_comb + [word], string[len(word):])
                    
        backtrack([], s)
        return res
                    
            
                
                