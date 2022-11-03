class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        neighbor = [set() for i in range(n)]
        
        for start, end in edges:
            neighbor[start].add(end)
            neighbor[end].add(start)
            
        print(neighbor)
        leaves = []
        for i in range(n):
            if len(neighbor[i]) == 1:
                leaves.append(i)
                
        print(leaves)
        remaining_nodes = n
        
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                surrounding = neighbor[leaf].pop()
                neighbor[surrounding].remove(leaf)
                
                if len(neighbor[surrounding]) == 1:
                    new_leaves.append(surrounding)
                    
            leaves = new_leaves
            
        return leaves
            