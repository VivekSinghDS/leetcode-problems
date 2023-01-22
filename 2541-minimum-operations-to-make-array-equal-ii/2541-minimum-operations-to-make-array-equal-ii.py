class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if nums1 == nums2:
            return 0
        if sum(nums1) != sum(nums2) or k == 0:
            return -1
        
        remaining = 0
        count = 0
        for i in range(len(nums1)):
            if nums1[i] == nums2[i]:
                continue 
                
            else:
                if nums1[i] > nums2[i]:
                    if (nums1[i] - nums2[i]) % k == 0:
                        remaining += (nums1[i] - nums2[i])
                        count += ((nums1[i] - nums2[i]) / k)
                    else:
                        return -1
                    
                else:
                    if (nums2[i] - nums1[i]) % k == 0:
                        remaining -= (nums2[i] - nums1[i])
                        count += ((nums2[i] - nums1[i]) / k)
                    else:
                        return -1
        return int(count/2) if remaining == 0 else -1
        
        