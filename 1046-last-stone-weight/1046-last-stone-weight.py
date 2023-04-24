class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones) == 1:
        #     return stones[0]
        stones = [-x for x in stones]
        heapify(stones)
        
        while stones:
            
            if len(stones) == 1:
                return -stones[0]
            
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 == stone_2:
                pass 
            
            elif stone_2 > stone_1:
                weight = stone_2 - stone_1
                heapq.heappush(stones, -weight)
                
            else:
                weight = stone_1 - stone_2
                heapq.heappush(stones, -weight)
                
        return 0
            
        