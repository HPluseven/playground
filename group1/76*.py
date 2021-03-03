class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1

        needCnt = len(t)
        left = 0
        res = (0, float('inf'))

        for right, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    if need[s[left]] == 0:
                        break
                    need[s[left]] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = (left, right)
                need[s[left]] += 1
                needCnt += 1
                left += 1

        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
