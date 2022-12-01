# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            nonlocal cur
            if node:
                inorder(node.left)
                node.left = None 
                
                cur.right = node
                cur = node 
                inorder(node.right)
                
        
        ans = cur = TreeNode(None)
        inorder(root)
        return ans.right
                
                
        