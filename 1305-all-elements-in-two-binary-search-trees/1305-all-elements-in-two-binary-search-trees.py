# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def get_inorder(root):
            res = []
            
            cur = root
            stack = []
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left 
                    
                cur = stack.pop()
                res.append(cur.val)
                
                cur = cur.right
            return res
        
        
        r1, r2 = get_inorder(root1), get_inorder(root2)
        r1_len, r2_len = len(r1), len(r2)
        i, j = 0, 0
        res = []
        while i < r1_len and j < r2_len:
            if r1[i] < r2[j]:
                res.append(r1[i])
                i += 1
                
            else:
                res.append(r2[j])
                j += 1
                
        while i < r1_len:
            res.append(r1[i])
            i += 1
            
        while j < r2_len:
            res.append(r2[j])
            j += 1
            
        return res
            
            
            
            
        
        
            