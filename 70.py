# time out
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dfs(n, 0)

    def dfs(self, n, count):
        if n < 0:
            return 0
        elif n == 0:
            return count + 1

        return count + self.dfs(n-1, count) + self.dfs(n-2, count)


class Solution:
    def climbStairs(self, n: int) -> int:
        p = 0
        q = 0
        r = 1

        for i in range(n):
            p = q
            q = r
            r = p + q

        return r
