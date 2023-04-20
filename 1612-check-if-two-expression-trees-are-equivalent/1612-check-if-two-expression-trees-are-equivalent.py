# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def dfs(node):
            if not node:
                return ""
            
            if node.val == "+":
                return dfs(node.left) + "+" + dfs(node.right)
            
            return node.val
        
        list_1 = dfs(root1)
        counter_1 = Counter(list_1.split("+"))
        
        list_2 = dfs(root2)
        counter_2 = Counter(list_2.split("+"))
        
        return counter_1 == counter_2