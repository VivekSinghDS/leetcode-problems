class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        @cache
        def is_good(n):
            if n == 1:
                return float('inf')
            
            elif n == 2 or n == 3:
                return 1
            
            number_of_ways = float('inf')
            if n >= 3:
                
                number_of_ways = min(number_of_ways, 1 + is_good(n - 3))
                
            if n >= 2:
                number_of_ways = min(number_of_ways, 1 + is_good(n - 2))
            return number_of_ways
            
        counter = Counter(tasks)
        total = 0
        for key in counter:
            value = is_good(counter[key])
            if value != float('inf'):
                total += value
                
            else:
                return -1
            
        return total
                
                