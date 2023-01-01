class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        char_to_string = {}
        string_to_char = {}
        
        if len(s) != len(pattern):
            return False
        for i, char in enumerate(pattern):
            if char in char_to_string:
                if char_to_string[char] != s[i]:
                    return False 
            
            if s[i] in string_to_char:
                if string_to_char[s[i]] != char:
                    return False
                
            else:
                char_to_string[char] = s[i]
                string_to_char[s[i]] = char
                
        return True
        