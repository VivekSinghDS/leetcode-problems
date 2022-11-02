# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        '''
        class Solution:
    
        def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

            successor = None

            while root:

                if p.val >= root.val:
                    root = root.right
                else:
                    successor = root
                    root = root.left

            return successor
        '''
        seen = False 
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            if seen:
                return cur
            if cur == p:
                seen = True
                
            cur = cur.right
        return None
            
        
        