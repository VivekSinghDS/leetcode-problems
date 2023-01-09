class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not(4 <= len(s) <= 12):
            return []
        
        res = []
        
        @cache
        def backtrack(index, current_combination):
            nonlocal res
            current_combination = list(current_combination)
            if len(current_combination) == 4:
                if index == len(s):
                    res.append(".".join(current_combination[:]))
                    
                return 
            
            num = ""
            for i in range(index, min(index + 3, len(s))):
                num += s[i]
                
                if num[0] == "0" and len(num) > 1:
                    break 
                    
                if 0 <= int(num) <= 255:
                    backtrack(i + 1, tuple(current_combination + [num]))
                    
        backtrack(0, tuple())
        return res
                
            
        