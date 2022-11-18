class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        memo = {}
        def check(offer, needs):
            for i in range(len(needs)):
                if offer[i] > needs[i]:
                    return False

            return True
        
        def dfs(price, special, needs, memo):
            if tuple(needs) in memo:
                return memo[tuple(needs)]

            min_cost = sum([needs[i] * price[i] for i in range(len(price))])

            for offer in special:
                if check(offer, needs):
                    left = [(needs[i] - offer[i]) for i in range(len(needs))]
                    min_cost = min(min_cost, offer[-1] + dfs(price, special, left, memo))

            memo[tuple(needs)] = min_cost
                
            return min_cost
        
        return dfs(price, special, needs, memo)
    
    
    
    
            
            
        
        