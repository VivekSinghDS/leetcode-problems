class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @cache
        def dfs(word):            
            res = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1:]
                if new_word in hash_set:
                    res = max(res, 1 + dfs(new_word))
                    
            return res

        hash_set = set()
        for word in words:
            hash_set.add(word)
            
        ans = 0 
        for word in words:
            ans = max(ans, dfs(word))
            
        return ans 
        