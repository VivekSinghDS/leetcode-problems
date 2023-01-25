class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        INF = float('inf')
        N = len(edges)
        def bfs(start):
            distances = [INF]*N
            queue = deque()
            queue.append(start)
            distances[start] = 0 
            
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    distance = distances[node]
                    
                    if edges[node] != -1 and distances[edges[node]] > distance:
                        distances[edges[node]] = distance + 1
                        queue.append(edges[node])
                        
            return distances
        
        
        d1 = bfs(node1)
        d2 = bfs(node2)
        best_index = -1
        best_value = float('inf')
        # print(d1, d2)
        for index, (x, y) in enumerate(zip(d1, d2)):
            d = max(x, y)
            if d != INF and best_value > d:
                best_index = index
                best_value = d
            
        return best_index
            