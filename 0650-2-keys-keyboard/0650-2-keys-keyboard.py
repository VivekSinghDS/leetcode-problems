class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dfs(clipboard, string):
            # print('-'*10)
            # print(clipboard, string)
            if clipboard > n or string > n:
                return float('inf')
            
            if string == n:
                return 0
            
            ans = float('inf')
            
            copy = dfs(string, string) if string > clipboard else float('inf')
            paste = dfs(clipboard, string + clipboard) if clipboard > 0 else float('inf')
            
            return 1 + min(copy, paste)
        
        return dfs(0, 1)
        