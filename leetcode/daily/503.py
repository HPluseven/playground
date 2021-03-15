# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         if not nums:
#             return []
#         max_ = max(nums)
#         n = len(nums)
#         ans = [-1] * n
#         arr = nums + nums[:]

#         for i in range(n):
#             for j in range(i+1,len(arr)):
#                 if arr[i] == max_:
#                     break
#                 if arr[j] > arr[i]:
#                     ans[i] = arr[j]
#                     break
#         return ans

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stk = []

        for i in range(2 * n - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ans[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ans
