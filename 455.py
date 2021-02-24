class Solution:
    # def findContentChildren(self, g, s):
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        start_j = 0

        for i in g:
            if start_j == len(s):
                return count

            for j, size in enumerate(s[start_j:]):
                if size >= i:
                    count += 1
                    start_j += j+1
                    break
                if j == len(s) - 1:
                    return count

        return count


class Solution:
    # optimize
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        m, n = len(g), len(s)
        i, j = 0, 0

        while i < m and j < n:
            while j < n and s[j] < g[i]:
                j += 1
            if j < n:
                count += 1

            i += 1
            j += 1

        return count


s = Solution()
print(s.findContentChildren([10, 9, 8, 7, 10, 9, 8, 7], [10, 9, 8, 7]))
