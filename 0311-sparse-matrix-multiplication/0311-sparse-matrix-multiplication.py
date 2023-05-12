class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, nA, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0]*n for _ in range(m)]
        rows = []
        for i in range(m):
            row = []
            for j in range(nA):
                if mat1[i][j]!=0:
                    row.append(j)
                    row.append(mat1[i][j])
            rows.append(row)

        for i in range(m):
            row  = rows[i]
            for j in range(0, len(row), 2):
                for k in range(n):
                    res[i][k] += mat2[row[j]][k] * row[j+1]
        return res