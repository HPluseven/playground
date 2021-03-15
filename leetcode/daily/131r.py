class Solution:
    # timeout
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        arr = []
        if not s:
            return ans
        if len(s) == 1:
            return [[s]]

        def backtrack(s, start, step):
            if step == len(s):
                if is_hui_wen(arr):
                    ans.append(arr[:])
            for idx in range(start, len(s)):
                char = s[idx]
                if arr:
                    arr.append(char)
                    last = len(arr)-1
                    backtrack(s, idx+1, step+1)
                    arr.pop(last)
                    last = len(arr) - 1
                    arr[last] += char
                    backtrack(s, idx+1, step+1)
                    arr[last] = arr[last][:-1]
                else:
                    arr.append(char)
                    step += 1

        def is_hui_wen(arr):
            for s in arr:
                if len(s) == 1:
                    continue
                i, j = 0, len(s)-1

                while i <= j:
                    if s[i] != s[j]:
                        return False
                    i += 1
                    j -= 1
            return True
        backtrack(s, 0, 0)
        return ans


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]

        # is wrong below
        # for i in range(n):
        #     for j in range(i+1, n):
        #         f[i][j] = (s[i] == s[j]) and f[i+1][j-1]
        ans = []
        ret = []

        def dfs(i):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()
        dfs(0)

        return ret


s = Solution()
print(s.partition('aab'))
