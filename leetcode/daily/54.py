import math
class Solution:
    def spiralOrder(self, matrix):
        # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        ret = []

        def flat_outer(matrix, i_start, i_end, j_start, j_end):
            ans = matrix[i_start][j_start:j_end+1]
            for i in range(i_start+1, i_end):
                ans.append(matrix[i][j_end])
            # print(matrix[i_end][j_start:j_end+1])
            ans += list(reversed(matrix[i_end][j_start:j_end+1]))
            for i in range(i_end-1, i_start, -1):
                ans.append(matrix[i][j_start])

            return ans
        for i in math.ceil((m-1) / 2):
            ret.append(flat_outer(matrix,))

        return flat_outer(matrix, 0, m-1, 0, n-1)


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
