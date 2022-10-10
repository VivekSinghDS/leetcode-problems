class Solution:
    def isValid(self, s: str) -> bool:
        opposites = {")":"(", 
                    "]":"[", 
                    "}":"{"}
        stack = []
        
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
                
            else:
                if not stack:
                    return False 
                
                element = stack.pop()
                if opposites[s[i]] != element:
                    return False 
                
        return not stack
        