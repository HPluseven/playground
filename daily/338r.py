# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         ans = []

#         for n in range(num+1):
#             count = 0
#             while n:
#                 count += 1
#                 n = n & (n-1)
#             ans.append(count)

#         return ans

# # dp1


# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         ans = [0]
#         highBit = 0

#         for n in range(1, num+1):
#             if n & (n-1) == 0:
#                 highBit = n
#             ans.append(ans[n - highBit] + 1)

#         return ans

# dp2
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]

        for i in range(1, num+1):
            ans.append(ans[i // 2] + (i & 1))

        return ans

# dp3
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]

        for i in range(1, num+1):
            ans.append(ans[i & (i-1)]+1)

        return ans

s = Solution()
print(s.countBits(4))
