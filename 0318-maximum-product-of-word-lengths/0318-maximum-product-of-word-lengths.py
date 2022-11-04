class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        '''
        class Solution:
            def maxProduct(self, words: List[str]) -> int:
                n = len(words)
                masks = [0] * n
                lens = [0] * n
                bit_number = lambda ch : ord(ch) - ord('a')

                for i in range(n):
                    bitmask = 0
                    for ch in words[i]:
                        # add bit number bit_number in bitmask
                        bitmask |= 1 << bit_number(ch)
                    masks[i] = bitmask
                    lens[i] = len(words[i])

                max_val = 0
                for i in range(n):
                    for j in range(i + 1, n):
                        if masks[i] & masks[j] == 0:
                            max_val = max(max_val, lens[i] * lens[j])
                return max_val
        '''
        def get_ord(ch):
            return ord(ch) - ord('a')
        
        # masks = [0]*len(words)
        hashmap = defaultdict(int)
        
        for i in range(len(words)):
            bitmask = 0
            for ch in words[i]:
                bitmask = bitmask | (1 << get_ord(ch))
                
            # masks[i] = bitmask 
            hashmap[bitmask] = max(hashmap[bitmask], len(words[i]))
        
        res = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    res = max(res, hashmap[x] * hashmap[y])
                    
        return res
            
                

        