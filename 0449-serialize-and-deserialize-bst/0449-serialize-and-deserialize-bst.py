# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(node):
            if not node:
                return [] 
            
            return dfs(node.left) + dfs(node.right) + [str(node.val)]
        
        postorder_string = ",".join(dfs(root))
        return postorder_string if root else ""
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None 
        
        data = [int(x) for x in data.split(',') if x]
        def helper(lower, upper):
            if not data or data[-1] < lower or data[-1] > upper:
                return None 

            value = data.pop()
            root = TreeNode(value)
            root.right = helper(value, upper)
            root.left = helper(lower, value)
            
            return root
        return helper(float('-inf'), float('inf'))
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans