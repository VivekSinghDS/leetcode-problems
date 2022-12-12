class Solution:
    def countHousePlacements(self, n: int) -> int:
        a, b = 1, 2
        for i in range(1, n):
            a, b = b, a + b
        return (b ** 2) % (10**9 + 7)
