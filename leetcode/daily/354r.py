class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)

        f = [1] * len(envelopes)

        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)
