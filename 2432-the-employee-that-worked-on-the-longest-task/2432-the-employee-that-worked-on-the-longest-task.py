class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        prev = 0
        mapper = {}
        
        for i, task in logs:
            if i in mapper:
                mapper[i] = max(task - prev, mapper[i])
            else:
                mapper[i] = task - prev
                
            prev = task
            
        maxTime = max(mapper.values())
        ans = float('inf')
        for key in mapper:
            if mapper[key] == maxTime:
                ans = min(ans, key)
                
        return ans 