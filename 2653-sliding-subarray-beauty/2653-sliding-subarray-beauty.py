from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        arr = SortedList()
        for r in range(len(nums)):
            arr.add(nums[r])
            
            if r - k >= 0:
                arr.remove(nums[r - k])
                
            if len(arr) >= k:
                value = arr[x - 1]
                ans.append(value if value < 0 else 0)
        return ans
            
            