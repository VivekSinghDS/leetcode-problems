# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = defaultdict(list)
        
        def dfs(node, layer):
            if not node:
                return layer 
            
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            
            level = max(left, right)
            output[level].append(node.val)
            
            return level + 1
        
        dfs(root, 0)
        return output.values()
        