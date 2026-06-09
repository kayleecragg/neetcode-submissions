class Solution:
    def climbStairs(self, n: int) -> int:

        # def memoi(n, cache):

        #     if n <= 1:
        #         return 1
        #     if n in cache:
        #         return cache[n]
        #     cache[n] = memoi(n - 1, cache) + memoi(n - 2, cache)
        #     return cache[n]

        # return (memoi(n, {}))

        # brute force

        # if n <= 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # haritha

        if (n == 1):
            return 1
        if (n == 2):
            return 2

        a = 1
        b = 2

        for i in range(3, n + 1):
            curr = a + b
            a = b
            b = curr
        
        return b