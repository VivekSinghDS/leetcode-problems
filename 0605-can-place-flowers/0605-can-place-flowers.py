class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ones_count = flowerbed.count(1)
        zero_count = len(flowerbed) - ones_count 
        if n == 0:
            return True
        if n > len(flowerbed) or n > zero_count:
            return False
        
        elif len(flowerbed) == 1:
            if n == 1:
                return True
            

        @cache
        def dfs(i):
            if i < 0:
                return 0 
            
            flag = False
            if i == 0:
                if flowerbed[i + 1] == 0:
                    flag = True
                    flowerbed[i] = 1
                    
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    flag = True
                    flowerbed[i] = 1
                
            elif flowerbed[i + 1] == flowerbed[i - 1] == 0:
                flag = True
                flowerbed[i] = 1
                
            total = max(flowerbed[i] + dfs(i - 2), dfs(i - 1))
            
            if flag:
                flowerbed[i] -= 1
            return total
        
        
        # print(ones_count)
        # print(dfs(len(flowerbed) - 1))
        
        return ones_count + n <= dfs(len(flowerbed) - 1) 
                
        