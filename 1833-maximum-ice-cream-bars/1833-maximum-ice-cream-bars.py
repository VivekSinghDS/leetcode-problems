class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        count = 0
        while coins and costs:
            ice_cream_cost = heapq.heappop(costs)
            
            if ice_cream_cost > coins:
                break 
                
            else:
                coins -= ice_cream_cost 
                count += 1
                
        return count
                
            
        