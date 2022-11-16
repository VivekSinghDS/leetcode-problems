class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        
        for parent, child in zip(ppid, pid):
            graph[parent].append(child)
            
        # print(graph)
        queue = deque()
        queue.append(kill)
        
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node)
                if node in graph:
                    queue.extend(graph[node])
                    
        return res