# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def search(node, value):
            if not node:
                return False 
            
            if value == node.val:
                return True
            
            if value > node.val:
                return search(node.right, value)
                
            else:
                return search(node.left, value)
            
        stack = []
        cur = root1
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            
            if search(root2, target - cur.val):
                return True
            cur = cur.right
        return False