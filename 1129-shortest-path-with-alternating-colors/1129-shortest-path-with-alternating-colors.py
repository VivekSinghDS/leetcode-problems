class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        for src, tar in redEdges:
            graph[src].add((tar, "red"))
            
        for src, tar in blueEdges:
            graph[src].add((tar, "blue"))
            
        # print(graph)
        res = [-1]*n
        
        queue = deque()
        queue.append((0, 0, None))
        distance = 0
        seen = set()
        while queue:
            node, distance, pre = queue.popleft()
            if res[node] == -1:
                res[node] = distance
            if not pre:
                for neighbor, color in graph[node]:
                    if (neighbor, color) not in seen:
                        seen.add((node, neighbor, color))
                        queue.append((neighbor, 1 + distance, color))
                    
            else:
                for neighbor, color in graph[node]:
                    if color != pre and (neighbor, color) not in seen:
                        seen.add((neighbor, color))
                        queue.append((neighbor, 1 + distance, color))
        
        
        return res
            
            
            