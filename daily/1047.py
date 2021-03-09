class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = S

        i = 0
        while i < len(ans):
            j = i + 1
            if j < len(ans) and ans[j] == ans[i]:
                ans = ans[:i]+ans[j+1:]
                i = 0
            else:
                i += 1

        return ans


s = Solution()
print(s.removeDuplicates("aaaaaaaaa"))
