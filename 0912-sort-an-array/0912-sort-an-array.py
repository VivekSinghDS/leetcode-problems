class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        output = []
        
        heapify(nums)

        while nums:
            output.append(heapq.heappop(nums))
            
        return output