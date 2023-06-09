class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        res = float('-inf')
        for array in arrays[1:]:
            res = max(res, max(abs(array[-1] - min_val), abs(array[0] - max_val)))
            min_val = min(min_val, array[0])
            max_val = max(max_val, array[-1])
        return res
        