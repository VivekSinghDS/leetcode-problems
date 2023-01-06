class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        res = []
        for rich, poor in richer:
            graph[poor].append(rich)
            
        # print(graph)
        @cache
        def dfs(node):
            quietest = quiet[node]
            ans_node = node
            for rich_neighbor in graph[node]:
                value, res_node = dfs(rich_neighbor)
                if quietest > value:
                    ans_node = res_node
                    quietest = value

                
            return (quietest, ans_node)
        res = []
        for key in range(len(quiet)):
            res.append(dfs(key)[1])
            
        return res
                
            
                
                
            
            
        