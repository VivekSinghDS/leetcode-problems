class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        
        for src, tar, cost in times:
            edges[src].append((tar, cost))
            
        minHeap = [(0, k)]
        seen = set()
        res = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node not in seen:
                seen.add(node)
                res = max(res, cost)
                
                for destination, new_cost in edges[node]:
                    heapq.heappush(minHeap, (cost + new_cost, destination))
                    
        return res if len(seen) == n else -1
        