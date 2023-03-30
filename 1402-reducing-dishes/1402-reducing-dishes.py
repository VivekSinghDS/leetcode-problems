class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        @cache
        def solve(index, time):
            if index >= len(satisfaction):
                return 0 
            
            include = (satisfaction[index]*(time + 1)) + solve(index + 1, time + 1)
            exclude = 0 + solve(index + 1, time)
            return max(include, exclude)
        
        satisfaction.sort()
        return solve(0, 0)
        
        