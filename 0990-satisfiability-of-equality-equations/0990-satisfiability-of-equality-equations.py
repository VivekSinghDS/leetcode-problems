class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(list)
        
        for equation in equations:
            if "==" in equation:
                equation = equation.split('==')
                for a, b in zip(equation[0], equation[1]):
                    graph[a].append(b)
                    graph[b].append(a)
                    
        # print(graph)
        def dfs(node, target, seen):
            if node == target:
                return False 
            
            elif node in seen:
                return True
            
            ans = True 
            seen.add(node)
            for neighbor in graph[node]:
                ans &= dfs(neighbor, target, seen)
                
            return ans 
        
        for equation in equations:
            seen = set()
            if "!=" in equation:
                equation = equation.split('!=')
                for a, b in zip(equation[0], equation[1]):
                    if not dfs(a, b, seen):
                        return False
                    
        return True
                
                    
        