class Solution:
    def climbStairs(self, n: int) -> int:

        def memoi(n, cache):

            if n <= 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = memoi(n - 1, cache) + memoi(n - 2, cache)
            return cache[n]

        return (memoi(n, {}))