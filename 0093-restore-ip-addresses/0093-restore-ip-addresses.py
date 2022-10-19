class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not 4 <= len(s) <= 12:
            return []
        
        res = []
        def backtrack(index, curr):
            nonlocal res
            if len(curr) == 4:
                if index == len(s):
                    res.append(".".join(curr))
                return 
            
            num = ''
            for i in range(index, min(index + 3, len(s))):
                num += s[i]
                
                if num[0] == '0' and len(num) > 1:
                    break 
                    
                if 0 <= int(num) <= 255:
                    curr.append(num)
                    backtrack(i + 1, curr)
                    curr.pop()
                    
        backtrack(0, [])
        return res

            
        