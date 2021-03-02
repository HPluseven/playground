class NumMatrix:

    def __init__(self, matrix):
        # def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] for _ in range(5)]
        _sums = self.sums

        for idx, row in enumerate(matrix):
            for cell in row:
                _sums[idx].append(_sums[idx][-1] + cell)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1, row2+1):
            result += (self.sums[i][col2+1]-self.sums[i][col1])
        return result


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0]*(n+1) for _ in range(m+1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i+1][j+1] = _sums[i][j+1] + \
                    _sums[i+1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums
        return _sums[row2+1][col2+1]-_sums[row1][col2+1] - _sums[row2+1][col1] + _sums[row1][col1]

        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)

        # [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]


m = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
              1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(m.sums)
print(m.sumRegion(1, 1, 2, 2))
