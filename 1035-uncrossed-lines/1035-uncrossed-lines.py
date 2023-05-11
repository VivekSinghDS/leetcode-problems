class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        matrix = [[0] * len(nums2) for _ in range(len(nums1))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0:
                    if nums1[r] == nums2[c]:
                        matrix[r][c] = max(1, matrix[r][c - 1])
                    else:
                        matrix[r][c] = max(matrix[r][c], matrix[r][c - 1])
                    continue
                
                if c == 0:
                    if nums1[r] == nums2[c]:
                        matrix[r][c] = max(1, matrix[r - 1][c])
                    else:
                        matrix[r][c] = max(matrix[r][c], matrix[r - 1][c])
                    continue
                if nums1[r] == nums2[c]:
                    matrix[r][c] = max(max(matrix[r - 1][c], matrix[r][c - 1]), 1 + matrix[r - 1][c - 1])
                else:
                    matrix[r][c] = max(matrix[r - 1][c], matrix[r][c - 1])
        
        max_val = max(i for x in matrix for i in x)
        return max_val
                    
                    
        