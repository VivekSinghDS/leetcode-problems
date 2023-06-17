class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        
        @cache
        def dfs(i, prev):
            if i >= len(arr1):
                return 0
            
            cost = float('inf')
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])
                
            idx = bisect_right(arr2, prev)
            if idx < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))
            return cost 
        
        res = dfs(0, -1)
        return res if res != float('inf') else -1