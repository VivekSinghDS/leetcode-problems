class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = [0]*n  # row[i] : is ith row already filled ?
        cols = [0]*n  # col[i] : is ith col already filled ?
        fillRows = 0
        fillCols = 0

        res = 0
        for i in range(len(queries)-1,-1,-1):
            typ,idx,val = queries[i]
            if typ == 0:
                if rows[idx] == 1:  # idx row already filled
                    continue
                res += (n - fillCols)*val   # fillCols cells already filled in the row idx
                rows[idx] = 1  # idx row is filled now
                fillRows += 1  # increase the fill rows count as idx row is filled now
            else:
                if cols[idx] == 1:  # idx col already filled
                    continue
                res += (n - fillRows)*val   # fillRows cells already filled in the col idx
                cols[idx] = 1  # idx col is filled now
                fillCols += 1  # increase the fill cols count as idx col is filled now
        return res