class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        @cache
        def backtrack(index):
            if index == len(s):
                #print(index, cur_comb)
                return 1
            
            elif s[index] == "0":
                return 0 
            
            ways = 0
            for i in range(index, len(s)):
                num = s[index:i + 1]
                if ((num[0] == "0" and len(num) == 1) or int(num) > k):
                    break
                ways += backtrack(i + 1)
                
            return ways % (10 ** 9 + 7)
        
        return backtrack(0) % (10 ** 9 + 7)
                