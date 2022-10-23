class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(list)
        
        for relation in equations:
            if "==" in relation:
                first, second = relation.split('==')
                graph[first].append(second)
                graph[second].append(first)
        
        print(graph)
        def dfs(node, target, visited):
            if node == target:
                return False 
            
            visited.add(node)
            ans = True 
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    ans &= dfs(neighbor, target, visited)
                
            return ans
            
            
        for relation in equations:
            if "!=" in relation:
                src, target = relation.split('!=')
                visited = set()
                if not dfs(src, target, visited):
                    return False
        
        return True 

        