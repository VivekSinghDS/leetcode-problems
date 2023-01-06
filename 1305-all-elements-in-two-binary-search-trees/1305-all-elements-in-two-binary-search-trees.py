# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def get_inorder(root):
            stack = []
            cur = root 
            res = []
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                    
                cur = stack.pop()
                res.append(cur.val)
                
                cur = cur.right
                
            return res 
        
        list_1, list_2 = get_inorder(root1), get_inorder(root2)
        # print(list_1, list_2)
        i, j = 0, 0
        res = []
        while i < len(list_1) and j < len(list_2):
            if list_1[i] > list_2[j]:
                res.append(list_2[j])
                j += 1
                
            else:
                res.append(list_1[i])
                i += 1
                
        while i < len(list_1):
            res.append(list_1[i])
            i += 1
            
        while j < len(list_2):
            res.append(list_2[j])
            j += 1
            
        return res
              
                
        