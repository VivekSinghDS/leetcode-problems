# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        cur = root
        stack = []
        prev = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
                
            cur = stack.pop()
            if prev:
                cur.val = cur.val + prev.val
                
            prev = cur
            cur = cur.left
            
        return root
                
            
            
            
        