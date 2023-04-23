class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dfs(index):
            if index == len(s):
                # print(cur_comb)
                return 1
            
            ways = 0
            
            for i in range(index, len(s)):
                num = s[index: i + 1]
                if int(num) > 26 or (num[0] == "0" and len(num) >= 1):
                    break 
                    
                ways += dfs(i + 1)
            return ways 
        
        return dfs(0)