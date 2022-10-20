class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        wordDict = set(wordDict)
        def dfs(dp, string):
            # print(string)
            if len(string) == 0:
                return True
            if string in dp:
                return dp[string]
            
            
            for word in wordDict:
                if string[:len(word)] == word and dfs(dp, string[len(word):]):
                    dp[string] = True 
                    return True 
                
            dp[string] = False 
            return False 
        
        return dfs(dp, s)
                    
            
            
        