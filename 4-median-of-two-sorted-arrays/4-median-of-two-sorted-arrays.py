class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        final = heapq.merge(nums1, nums2)
        final = list(final)
        length = len(final)
        if len(final) % 2 == 1:
            return final[(length // 2)]
        
        else:
            left = int(length / 2) - 1
            right = int(length / 2)

            return (final[left] + final[right])/2
        