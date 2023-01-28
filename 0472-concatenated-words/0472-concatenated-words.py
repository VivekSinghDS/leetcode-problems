class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        lookup = set(words)
        
        
        def dfs(word):
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if((prefix in lookup and suffix in lookup)
                  or prefix in lookup and dfs(suffix)):
                    return True 
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res
        