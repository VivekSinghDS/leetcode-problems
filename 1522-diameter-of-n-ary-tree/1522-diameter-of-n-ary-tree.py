"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        def dfs(node):
            nonlocal diameter
            if len(node.children) == 0:
                return 0 
            
            m1, m2 = 0, 0
            for children in node.children:
                parent_height = 1 + dfs(children)
                
                if parent_height > m1:
                    m1, m2 = parent_height, m1
                    
                elif parent_height > m2:
                    m2 = parent_height
                    
            total_distance = m1 + m2 
            diameter = max(diameter, total_distance)
            
            return m1
        
        diameter = 0
        dfs(root)
        return diameter