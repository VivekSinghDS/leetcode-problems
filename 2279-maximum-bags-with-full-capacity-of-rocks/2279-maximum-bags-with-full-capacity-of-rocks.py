class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = [i - j for (i, j) in zip(capacity, rocks)]
        # print(remaining)
        
        heapify(remaining)
        count = 0
        while remaining and additionalRocks:
            remaining_capacity = heapq.heappop(remaining)
            # print(remain, additionalRocks)
            if remaining_capacity == 0:
                count += 1
            
            else:
                while remaining_capacity > 0 and additionalRocks:
                    subtracter = min(additionalRocks, remaining_capacity)
                    remaining_capacity -= subtracter
                    additionalRocks -= subtracter
                
                if remaining_capacity == 0:
                    count += 1        
        return count