class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        for word in words:
            word_to_pattern = {}
            pattern_to_word = {}
            
            for character, pword in zip(word, pattern):
                if character in word_to_pattern and word_to_pattern[character] != pword:
                    break 
                    
                else:
                    word_to_pattern[character] = pword
                    
                if pword in pattern_to_word and pattern_to_word[pword] != character:
                    break
                    
                else:
                    pattern_to_word[pword] = character
                    
            else:
                res.append(word)
        return res
        