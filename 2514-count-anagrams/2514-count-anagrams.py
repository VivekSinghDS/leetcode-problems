class Solution:
    def countAnagrams(self, s: str) -> int:

        def get(word):
            n = math.factorial(len(word))

            for v in Counter(word).values():
                n //= math.factorial(v)

            return int(n) % (10**9 + 7)

        total = 1  
        for word in s.split():
            total *= get(word)

        return total % (10**9 + 7)
