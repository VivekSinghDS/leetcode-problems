class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        ans = 0
        
        @cache
        def dfs(index, heads):
            if index >= len(prob):
                if heads == target:
                    return 1
                return 0
            current_probability = prob[index]
            if target < heads:
                return (1 - current_probability) * dfs(index + 1, heads)
            
            include = current_probability * dfs(index + 1, heads + 1)
            exclude = (1 - current_probability) * dfs(index + 1, heads)
            return include + exclude
        
        return dfs(0, 0)
            