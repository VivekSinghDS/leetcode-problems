class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(index, cur_comb):
            nonlocal res
            if index == len(s):
                
                if len(cur_comb) == 4:
                    # print(cur_comb)
                    res.append(".".join(cur_comb))
                
                return 
            
            num = ""
            for i in range(index, len(s)):
                num += s[i]
                
                if num[0] == "0" and len(num) > 1:
                    break
                    
                if 0 <= int(num) <= 255:
                    backtrack(i + 1, cur_comb + [num])
                    
        backtrack(0, [])
        return res
        