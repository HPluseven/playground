class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(visited, nums):
            if len(visited) == len(nums):
                temp = visited[:]
                res.append(temp)
                return

            for num in nums:
                if num not in visited:
                    visited.append(num)
                    dfs(visited, nums)
                    visited.pop()
        dfs([], nums)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res
