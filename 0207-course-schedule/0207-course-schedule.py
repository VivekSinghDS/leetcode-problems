class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for current, pre in prerequisites:
            graph[current].append(pre)
        
        @cache
        def dfs(current):
            if current in seen:
                return False
            
            elif graph[current] == []:
                return True
            
            ans = True
            seen.add(current)
            for pre in graph[current]:
                if not dfs(pre):
                    return False
                
            seen.remove(current)
            if ans:
                graph[current] = []
            
            return ans
        ans = True
        seen = set()
        for i in range(n):
            
            ans &= dfs(i)
        return ans
                
        