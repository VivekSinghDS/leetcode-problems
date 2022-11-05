class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix = [y for x in matrix for y in x]
        heapify(matrix)
        
        while k:
            element = heapq.heappop(matrix)
            k -= 1
            # print(element, k)
            if k == 0:
                return element 
            
            
                
                
        