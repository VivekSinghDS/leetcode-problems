class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        for i in range(len(pushed)):
            stack.append(pushed[i])
            
            while stack and popped and stack[-1] == popped[0]:
                # print(i)
                stack.pop()
                popped.pop(0)
                
        while popped and stack:
            if popped and not stack:
                return False 
            
            elif popped[0] != stack[-1]:
                return False 
            
            else:
                popped.pop(0)
                stack.pop()
                
        return False if stack or popped else True