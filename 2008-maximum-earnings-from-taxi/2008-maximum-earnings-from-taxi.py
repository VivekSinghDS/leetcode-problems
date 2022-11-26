class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rideInfo = defaultdict(list)
        
        for start, end, tip in rides: # store the information about the rides
            rideInfo[start].append((end, end - start + tip))
            
        max_cost_from_i = [0]*(n + 1) # the maximum amount we can get from ith position
        
        for start in range(n - 1, 0, -1): # check from the last whether there is a start of some ride or not
            for end, earned_amount in rideInfo[start]:
                max_cost_from_i[start] = max(max_cost_from_i[start], max_cost_from_i[end] + earned_amount) 
                # Above we have two options, one being take this ride into account and add from the end the remaining we can get
                # The second choice is simply not include it. 
                
            max_cost_from_i[start] = max(max_cost_from_i[start], max_cost_from_i[start + 1])
            # Now, we see whether previously, have we computed the best value in start + 1 or not
            
        return max_cost_from_i[1]
        