class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, visited, nums):
            res.append(visited[:])
            if len(visited) == len(nums) or idx == len(nums):
                return

            for i, num in enumerate(nums[idx:]):
                if num not in visited:
                    visited.append(num)
                    backtrack(i+idx+1, visited, nums)
                    visited.pop()

        res = []
        backtrack(0, [], nums)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur):
            if cur == n:
                res.append(t[:])
                return

            t.append(nums[cur])
            dfs(cur+1)
            t.pop()
            dfs(cur+1)

        n = len(nums)
        t = []
        res = []
        dfs(0)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        mask = 0
        while mask < (1 << n):
            t = []
            for i in range(n):
                if mask & (1 << i):
                    t.append(nums[i])
            ans.append(t)
            mask += 1
        return ans


s = Solution()
print(s.subsets([1, 2, 3]))
