class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i : [] for i in range(len(points))}
        minHeap = []
        for i in range(len(points)):
            x1, y1 = points[i]
            
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                
                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((distance, j))
                graph[j].append((distance, i))
                
        # print(graph)
        seen = set()
        minHeap = [(0, 0)]
        res = 0
        while len(seen) < len(points):
            distance, node = heapq.heappop(minHeap)
            # print(distance, node)
            if node in seen:
                continue 
                
            seen.add(node)
            res += distance
            for neighborCost, neighbor in graph[node]:
                heapq.heappush(minHeap, (neighborCost, neighbor))
                
        return res
            
            
                
        