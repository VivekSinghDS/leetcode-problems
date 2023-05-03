class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        l1 = []
        l2 = []
        for n in nums1:
            if n not in nums2:
                l1.append(n)
                
        for n in nums2:
            if n not in nums1:
                l2.append(n)
                
        return [l1, l2]
                
                
        