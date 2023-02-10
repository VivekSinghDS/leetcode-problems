class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        n = len(s)
        sections = ceil(n / (numRows + numRows - 2))
        no_of_cols = sections * (numRows - 1)
        
        matrix = [[' '] * no_of_cols for i in range(numRows)]
        cur_row, cur_col = 0, 0
        cur_string_index = 0
        
        while cur_string_index < n:
            while cur_row < numRows and cur_string_index < n:
                matrix[cur_row][cur_col] = s[cur_string_index]
                cur_string_index += 1
                cur_row += 1
            
            cur_row -= 2
            cur_col += 1
            
            while cur_row > 0 and cur_col < no_of_cols and cur_string_index < n:
                matrix[cur_row][cur_col] = s[cur_string_index]
                
                cur_row -= 1
                cur_col += 1
                cur_string_index += 1
                
        # print(matrix)
        answer = ""
        for row in matrix:
            answer += "".join(row)
            
        return(answer.replace(" ", ""))
        