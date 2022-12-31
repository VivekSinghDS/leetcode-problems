class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        def count(string):
            # print(string)
            res = 0
            for char in string:
                if (char == "a" or 
                    char == "e" or 
                    char == "i" or 
                    char == "o" or 
                    char == "u"):
                    # print(char)
                    res += 1
                    
            return res
        
        # print(len(s)/2)
        # print(count(s[:int(len(s)/2)]), count(s[int(len(s)/2):]))
        return count(s[:int(len(s)/2)].lower()) == count(s[int(len(s)/2):].lower())
                    
                