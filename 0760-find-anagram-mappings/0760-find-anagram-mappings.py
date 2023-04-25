class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {val: index for index, val in enumerate(nums2)}
        res = []
        # print(n1)
        for value in nums1:
            res.append(n1[value])
            
        return res
        