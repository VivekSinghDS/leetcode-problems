class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-num for num in piles]
        heapify(piles)
        while k:
            element = -1 * heapq.heappop(piles)
            element -= floor(element / 2)
            
            heapq.heappush(piles, -element)
            
            k -= 1
            
        return -1*sum(piles)
            
        