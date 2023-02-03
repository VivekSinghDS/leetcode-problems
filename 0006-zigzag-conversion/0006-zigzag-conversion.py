class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        # print(rows)
        row = 0
        direction = 1

        for c in s:
            # print(rows)
            rows[row].append(c)
            row += direction

            if row == 0 or row == numRows - 1:
                direction *= -1
                
            # print('-'*10)
                
        # print(rows)
        ans = ["".join(row) for row in rows]
        return "".join(ans)
        