class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        res = -1
        def dfs(i):
            nonlocal res
            if i in visited:
                return (i,1)
            visited.add(i)
            if edges[i]!=-1:
                a,b = dfs(edges[i])
                if a!=i:
                    return (a,b+1)
                else:
                    res = max(res,b)
                    return (a,1)
            return (-1,-1)
            
        for i in range(len(edges)):
            if i not in visited:
                dfs(i)
        return res