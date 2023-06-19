class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain = 0
        current = 0
        for n in gain:
            current += n
            max_gain = max(max_gain, current)
        return max_gain
            
            
        