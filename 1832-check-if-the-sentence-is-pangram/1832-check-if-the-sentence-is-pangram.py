class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = 0
        
        for char in sentence:
            cur_bit = 0
            cur_bit = 1 << (ord(char) - ord('a'))
            
            seen |= cur_bit
            
        return seen == (1 << 26) - 1
        