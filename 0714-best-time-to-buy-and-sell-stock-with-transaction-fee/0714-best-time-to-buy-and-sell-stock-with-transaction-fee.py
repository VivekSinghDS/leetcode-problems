class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 2023/06/21 21:36PM -> 21:44PM
        @cache
        def dfs(i, hold):
            if i >= len(prices):
                return 0
            # recursive
            if not hold:
                # buy stock / skip stock
                return max(-prices[i] + dfs(i + 1, not hold), dfs(i + 1, hold))
            else:
                # hold stock / sell stock
                return max(dfs(i + 1, hold), prices[i] + dfs(i + 1, not hold) - fee)
        return dfs(0, False)