class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(index):
            if index >= len(questions):
                return 0 
            points, next_ = questions[index]
            include = points + dfs(index + next_ + 1)
            exclude = dfs(index + 1)
            return max(include, exclude)
        return dfs(0)
        '''
        @cache
        def dfs(index, current_points):
            if index >= len(questions):
                return current_points
            points, next_ = questions[index]
            include = dfs(index + next_ + 1, current_points + points)
            exclude = dfs(index + 1, current_points)
            return max(include, exclude)
        
        return dfs(0, 0)
        '''
        

            
            
        