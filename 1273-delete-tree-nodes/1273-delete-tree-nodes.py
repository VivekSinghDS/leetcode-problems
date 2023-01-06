class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        graph = defaultdict(list)
        
        for child, parent in enumerate(parent):
            graph[parent].append(child)
            
            
        # print(graph)
        def dfs(node):
            total_nodes = 1
            cur_sum = value[node]
            
            for child in graph[node]:
                children_sum, children_node_count = dfs(child)
                
                cur_sum += children_sum
                total_nodes += children_node_count
                
            if cur_sum == 0:
                 total_nodes = 0 
                    
            return (cur_sum, total_nodes)
        
        return dfs(0)[1]
        