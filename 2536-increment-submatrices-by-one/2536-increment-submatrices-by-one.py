class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*(n) for i in range(n)]
        
        
        for x1, y1, x2, y2 in queries:
            
            while x1 != x2 + 1:
                
                matrix[x1][y1] += 1
                if y2 + 1 < len(matrix):
                    matrix[x1][y2 + 1] -= 1
                    
                x1 += 1
        # print(matrix)       
        
        for r in range(len(matrix)):
            running_sum = 0 
            for c in range(len(matrix[0])):
                matrix[r][c] += running_sum 
                running_sum = matrix[r][c]
            

            
        return(matrix)
            
        # for i in range(len(matrix))
            
        
        