# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        prev = None
        ans = float('inf')
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            if prev:
                ans = min(ans, abs(cur.val - prev.val))
            
            prev = cur
            cur = cur.right
            
        return ans
                
            
        