# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        def dfs(node, parent_exist):
            if not node:
                return None 
            
            if node.val in to_delete:
                node.left = dfs(node.left, False)
                node.right = dfs(node.right, False)
                return None 
            
            else:
                if not parent_exist:
                    res.append(node)
                    
                node.left = dfs(node.left, True)
                node.right = dfs(node.right, True)
                return node
        dfs(root, False)
        return res
        