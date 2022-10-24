class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
                
        def backtrack(remain, cur_comb, index):
            if len(cur_comb) > 0:
                res.append(cur_comb + [remain])

            
            for i in range(index, int(remain ** 0.5) + 1):
                if remain % i == 0:
                    cur_comb.append(i)
                    backtrack(remain // i, cur_comb, i)
                    cur_comb.pop()
                
        backtrack(n, [], 2)
        return res
        