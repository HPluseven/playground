class Solution:
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    def islandPerimeter(self, grid):
        perimeter = 0

        m, n = len(grid), len(grid[0]) if grid else 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i-1 < 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    if i+1 >= m or grid[i+1][j] == 0:
                        perimeter += 1
                    if j-1 < 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    if j+1 >= n or grid[i][j+1] == 0:
                        perimeter += 1
        return perimeter


s = Solution()
opts = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
opts1 = [[1]]
opt3 = [[1,1],[0,0]]
ret = s.islandPerimeter(opt3)
print(ret)
