# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        mapper = {}
        res = []
        
        def dfs(node):
            if not node:
                return 0
            
            left_part = dfs(node.left)
            right_part = dfs(node.right)
            
            val = node.val + left_part + right_part
            mapper[val] = 1 + mapper.get(val, 0)
            
            return val
        
        dfs(root)
        max_val = max(mapper.values())
        for key in mapper:
            if mapper[key] == max_val:
                res.append(key)
                
        return res
        
            
        