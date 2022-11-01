class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def check_palindrome():
            one_odd = False 
        
            counter = Counter(s)

            for key in counter:
                if counter[key] % 2 == 1:
                    if one_odd == True:
                        return False 

                    one_odd = True 

            return True
        
        counter = Counter(s)
        if not check_palindrome():
            print('i get here')
            return []
        
        res = []
        def backtrack(counter, curr_string):
            nonlocal res
            if len(curr_string) == len(s):
                
                res.append(curr_string)
                return 
            
            for key in counter:
                if counter[key] > 0:
                    counter[key] -= 2
                    
                    backtrack(counter, key+curr_string+key)
                    
                    counter[key] += 2
        
        # print(counter)
        odd_letter = None 
        for key in counter:
            if counter[key] % 2 == 1:
                odd_letter = key
                counter[key] -= 1
                
        string = "" if not odd_letter else odd_letter
        backtrack(counter, string)
        
        return(res)
                    
            
        
        
        