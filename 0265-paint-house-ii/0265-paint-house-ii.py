class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
    
        n = len(costs)
        k = len(costs[0])
        
        for house in range(1, n):
            min_color, second_min = None, None 
            
            for color in range(k):
                cost = costs[house-1][color]
                if min_color is None or cost < costs[house - 1][min_color]:
                    second_min = min_color 
                    min_color = color
                    
                elif second_min is None or cost < costs[house - 1][second_min]:
                    second_min = color
                    
            for color in range(k):
                if color == min_color:
                    costs[house][color] += costs[house - 1][second_min]
                else:
                    costs[house][color] += costs[house - 1][min_color]
                    
        return (min(costs[-1]))