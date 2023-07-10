class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        def dfs(node, count):
            nonlocal res
            if node:
                if not node.left and not node.right:
                    res = min(res, count)
                    return 
                
                if count + 1 < res:
                    dfs(node.left, count + 1)
                    dfs(node.right, count + 1)
        
        dfs(root, 1)
        return res if root else 0