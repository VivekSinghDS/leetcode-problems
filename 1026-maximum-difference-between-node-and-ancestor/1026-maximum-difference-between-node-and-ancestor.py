class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        abs_max = float('-inf')
        def dfs(node):
            nonlocal abs_max
            if not node:
                return None 
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            if not left and not right:
                return (node.val, node.val)
            
            cur_min = None 
            cur_max = None 
            if left and not right:
                cur_min = min(node.val, left[0])
                cur_max = max(node.val, left[1])
                abs_max = max(abs_max, abs(node.val - cur_min), abs(node.val - cur_max))
                
            if right and not left:
                cur_min = min(node.val, right[0])
                cur_max = max(node.val, right[1])
                abs_max = max(abs_max, abs(node.val - cur_min), abs(node.val - cur_max))
                
            if left and right:
                cur_min = min(node.val, left[0], right[0])
                cur_max = max(node.val, right[1], left[1])
                abs_max = max(abs_max, abs(node.val - cur_min), abs(node.val - cur_max))
            return (cur_min, cur_max)
        dfs(root)
        return(abs_max)
