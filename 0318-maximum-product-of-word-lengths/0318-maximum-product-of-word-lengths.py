class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def get_ord(ch):
            return ord(ch) - ord('a')
        
        masks = [0]*len(words)
        length = [0]*len(words)
        
        for i in range(len(words)):
            bitmask = 0
            for ch in words[i]:
                bitmask = bitmask | (1 << get_ord(ch))
                
            masks[i] = bitmask 
            length[i] = len(words[i])
        
        res = 0
        for i in range(len(words)):
            for j in range(i):
                if masks[i] & masks[j] == 0:
                    res = max(res, length[i] * length[j])
                    
        return res
            
                

        