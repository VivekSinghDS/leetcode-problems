class Solution:
    def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        
        jobs = sorted(zip(s, e, p))
        
        @lru_cache(None)
        def dfs(i):
            if i >= len(jobs) : return 0
            k = bisect_left(jobs, jobs[i][1], key = lambda j: j[0])
            return max(dfs(i+1), jobs[i][2] + dfs(k))
            
        return dfs(0)