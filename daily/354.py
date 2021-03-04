class Solution:
    def maxEnvelopes(self, envelopes) -> int:
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envs = sorted(envelopes, key=lambda x: x[0]*x[1])
        n = len(envs)
        groups = [0]
        max_num = 0

        for i in range(n):
            count = 1
            last = envs[i]
            for j in range(i+1, n):
                cur = envs[j]
                if last[0] < cur[0] and last[1] < cur[1]:
                    last = cur
                    count += 1
            max_num = max(max_num, count)
            groups.append(count)
            if max_num > n-i:
                break

        return max(groups)


s = Solution()
print(s.maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]))
