class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        tree = defaultdict(list)
        
        for src, tar in edges:
            tree[src].append(tar)
            tree[tar].append(src)
        
        diameter = 0
        def dfs(node, parent):
            nonlocal diameter 
            
            m1, m2 = 0, 0
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue 
                    
                parent_height = dfs(neighbor, node)
                if m1 < parent_height:
                    m1, m2 = parent_height, m1
                    
                else:
                    m2 = max(m2, parent_height)
                    
            diameter = max(diameter, m1 + m2)
            return 1 + max(m1, m2)
            
        
        seen = set()
        dfs(0, -1)
        return diameter