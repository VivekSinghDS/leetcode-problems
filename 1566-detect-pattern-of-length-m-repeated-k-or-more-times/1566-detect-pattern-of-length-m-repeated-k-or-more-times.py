class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        len_arr = len(arr)
        for lo in range(len_arr - m * k + 1):
            pattern = arr[lo:lo + m]
            if arr[lo:lo + k * m] == pattern * k:
                return True
        return False
            
        