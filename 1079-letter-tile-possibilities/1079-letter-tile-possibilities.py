class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        counter = Counter(tiles)
        res = 0

        def backtrack(counter, cur_comb):
            nonlocal res
            if len(cur_comb) > 0:
                res += 1
                
            for key in counter:
                if counter[key] > 0:
                    counter[key] -= 1
                    backtrack(counter, cur_comb + key)
                    counter[key] += 1
                    
        backtrack(counter, "")
        return res

        
        