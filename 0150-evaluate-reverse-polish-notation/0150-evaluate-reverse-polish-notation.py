class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        res = 0
        
        for token in tokens:
            
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            
                
            else:
                res = 0
                second_element = stack.pop()
                first_element = stack.pop()
                if token == "+":
                    res = second_element + first_element
                    
                elif token == "-":
                    res = first_element - second_element
                    
                elif token == "*":
                    res = first_element * second_element 
                    
                else:
                    res = int(first_element / second_element)
                    
                stack.append(res)
        return(stack[0])
            
                    
                    
                    
                    
        