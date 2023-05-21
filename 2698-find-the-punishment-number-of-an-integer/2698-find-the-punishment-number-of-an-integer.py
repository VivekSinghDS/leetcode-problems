class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(index, current_sum):
            nonlocal res
            if index >= len(number):
                if current_sum == target:
                    if not res:
                        res = True
                return 
            
            elif current_sum > target:
                return 
            
            
            for j in range(index + 1, len(number) + 1):
                new_sum = int(number[index : j])
                dfs(j, current_sum + new_sum)
                
        ans = 1
        for i in range(2, n + 1):
            number = str(i ** 2)
            target = i
            res = False
            dfs(0, 0)
            
            if res:
                ans += int(number)
        return ans