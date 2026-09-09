class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # nums = list(range(n + 1))
        # nums.sort()

        combs = []
        
        def helper(i, cur):

            if len(cur) == k:
                combs.append(cur.copy())
                return

            if i > n:
                return

            cur.append(i)
            helper(i + 1, cur)
            cur.pop()

            helper(i + 1, cur)

        helper(1, [])
        return combs
