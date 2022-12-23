class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        graph = defaultdict(list)
        for node in range(nodes):
            graph[parent[node]].append(node)

        def dfs(node):
            total_nodes = 1
            cur_sum = value[node]
            
            for neighbor in graph[node]:
                sum_count, nodes_count = dfs(neighbor)
                
                total_nodes += nodes_count
                cur_sum += sum_count 
                
            if cur_sum == 0:
                total_nodes = 0
                
            return (cur_sum, total_nodes)
        
        return dfs(0)[1]
                
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        

        