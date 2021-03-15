class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), (len(nums[0]) if nums else 0)
        if m * n != r * c:
            return nums

        temp = []
        for row in nums:
            for cell in row:
                temp.append(cell)

        ans = [temp[i:i+c] for i in range(0, m*n, c)]
        return ans


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), (len(nums[0]) if nums else 0)
        if m * n != r * c:
            return nums

        ans = [[0] * c for _ in range(r)]
        for i in range(m*n):
            ans[i // c][i % c] = nums[i // n][i % n]
        return ans
