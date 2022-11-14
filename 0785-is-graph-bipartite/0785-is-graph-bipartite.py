class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = {}
        
        for node in range(len(graph)):
            if node not in colored:
                colored[node] = 1
        
            # print(colored)
            queue = [node]
            while queue:

                cur_node = queue.pop(0)

                for neighbor in graph[cur_node]:   
                    if neighbor not in colored:
                        colored[neighbor] = -colored[cur_node]
                        queue.append(neighbor)
                    elif colored[neighbor] == colored[cur_node]:
                        return False
                        
        return True
        
        

                
        