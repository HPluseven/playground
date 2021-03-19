import math


# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         n = math.ceil(math.sqrt(c))+1

#         for i in range(n, -1, -1):
#             for j in range(i, -1, -1):
#                 if i ** 2 + j ** 2 == c:
#                     return True

#         return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0

        while(a**2 <= c):
            b = math.sqrt(c-a**2)
            if b == int(b):
                return True
            a += 1
        return False


s = Solution()
print(s.judgeSquareSum(1))
