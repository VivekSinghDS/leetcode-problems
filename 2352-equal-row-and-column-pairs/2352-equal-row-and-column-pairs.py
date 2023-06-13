class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_set = defaultdict(int)
        
        for g in grid:
            # print(g)
            row_set[tuple(g)] += 1
        count = 0
        counter = 0
        # print('-'*10)
        while counter < len(grid):
            
            for i in range(len(grid)):
                col_set = []
                for j in range(len(grid)):
                    col_set.append(grid[j][i])
                    
                
                # print(col_set)
                if tuple(col_set) in row_set:
                    count += row_set[tuple(col_set)]
                counter += 1
                col_set = []
        return count
                
            
        