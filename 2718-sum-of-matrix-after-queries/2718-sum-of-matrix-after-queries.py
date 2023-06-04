class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_filled_count = col_filled_count = 0
        rows = [0]*n
        cols = [0]*n
        res = 0
        for i in range(len(queries) - 1, -1, -1):
            type_, index, value = queries[i]
            if type_:# column case 
                if cols[index]:
                    continue   
                res += (n - row_filled_count)*value
                cols[index] = 1 
                col_filled_count += 1 
            else: # rows case 
                if rows[index]:
                    continue 
                
                res += (n - col_filled_count)*value
                rows[index] = 1
                row_filled_count += 1
        return res
                
                
            
        