class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_s = {}
        s_pattern = {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            # print(s_pattern, pattern_s)
            # print(pattern[i], s[i])
            if pattern[i] in pattern_s:
                if pattern_s[pattern[i]] != s[i]:
                    return False 
                
            if s[i] in s_pattern:
                if s_pattern[s[i]] != pattern[i]:
                    return False
                
            else:
                pattern_s[pattern[i]] = s[i]
                s_pattern[s[i]] = pattern[i]
                
            # print('-'*10)
                
        return True
            
        