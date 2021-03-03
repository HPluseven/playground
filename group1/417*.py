class Solution:
    # dfs
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        m, n = len(matrix), len(matrix[0])
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        atlantic = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    self.dfs(matrix, pacific, i, j, matrix[i][j])
                if i == m - 1 or j == n - 1:
                    self.dfs(matrix, atlantic, i, j, matrix[i][j])

        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])

        return res

    def dfs(self, matrix, aux, i, j, pre):
        if i < 0 or j < 0 or i > len(matrix)-1 or j > len(matrix[0])-1 or aux[i][j] == 1 or matrix[i][j] < pre:
            return
        aux[i][j] = 1

        self.dfs(matrix, aux, i-1, j, matrix[i][j])
        self.dfs(matrix, aux, i+1, j, matrix[i][j])
        self.dfs(matrix, aux, i, j-1, matrix[i][j])
        self.dfs(matrix, aux, i, j+1, matrix[i][j])


class Solution:
    # bfs
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        m, n = len(matrix), len(matrix[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    self.bfs(matrix, pacific, i, j, matrix[i][j])
                if i == m - 1 or j == n - 1:
                    self.bfs(matrix, atlantic, i, j, matrix[i][j])

        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])

        return res

    def bfs(self, matrix, aux, i, j, pre):
        m, n = len(matrix), len(matrix[0])
        queue = [(i, j, pre)]

        while queue:
            i, j, pre = queue.pop(0)
            if i < 0 or j < 0 or i > m-1 or j > n-1 or aux[i][j] == 1 or matrix[i][j] < pre:
                continue
            aux[i][j] = 1
            queue.append((i-1, j, matrix[i][j]))
            queue.append((i+1, j, matrix[i][j]))
            queue.append((i, j-1, matrix[i][j]))
            queue.append((i, j+1, matrix[i][j]))
