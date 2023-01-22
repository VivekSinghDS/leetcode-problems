class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(s, memo):
            if len(s) == 1:
                return [[s]]
            
            elif len(s) == 0:
                return [[]]
            
            if s in memo:
                return memo[s]
            
            res = []
            for i in range(1, len(s) + 1):
                candidate = s[:i]
                if candidate == candidate[::-1]:
                    for partition in dfs(s[i:], memo):
                        res.append([candidate] + partition)
                        
            memo[s] = res
            return res
        return dfs(s, {})
        