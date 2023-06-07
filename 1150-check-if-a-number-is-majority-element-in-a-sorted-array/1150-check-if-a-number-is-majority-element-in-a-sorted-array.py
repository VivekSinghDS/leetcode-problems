class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        counter = Counter(nums)
        length = len(nums)
        
        
        if target in counter and counter[target] > length / 2:
            return True 
        return False
            