class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x : x[0])
        
        @cache
        def dfs(index, remaining, previous_meet_ended):
            if remaining == 0 or index >= len(events):
                return 0
            
            value = events[index][2]
            start_time = events[index][0]
            end_time = events[index][1]
            if previous_meet_ended < start_time:
                include = value + dfs(index + 1, remaining - 1, end_time)
                exclude = dfs(index + 1, remaining, previous_meet_ended)
                
            else:
                include = 0
                exclude = dfs(index + 1, remaining, previous_meet_ended)
            return max(include, exclude)
        return dfs(0, k, 0)
            
            
        