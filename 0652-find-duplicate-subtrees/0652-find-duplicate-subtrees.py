# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        mapper = {}
        
        def dfs(node, preorder_path):
            if not node:
                return "#"
            
            preorder_path += ",".join([str(node.val), dfs(node.left, preorder_path), dfs(node.right, preorder_path)])
            
            if preorder_path in mapper:
                mapper[preorder_path] += 1
                
                if mapper[preorder_path] == 2:
                    res.append(node)
                    
            else:
                mapper[preorder_path] = 1
                
            return preorder_path
        
        dfs(root, "")
        return res
                
            
                    
                    
        