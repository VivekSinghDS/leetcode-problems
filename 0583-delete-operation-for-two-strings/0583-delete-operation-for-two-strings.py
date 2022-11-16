class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return abs(len(word1) - dp[-1][-1]) + abs(len(word2) - dp[-1][-1])
        