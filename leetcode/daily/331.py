# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         if not preorder:
#             return False

#         preorderArr = preorder.split(',')

#         n = len(preorderArr)
#         stk = []

#         for i in range(n):
#             node = preorderArr[i]
#             if not stk and 0 < i < n:
#                 return False
#             elif stk:
#                 stk[-1] += 1
#             if stk and stk[-1] == 2:
#                 stk.pop()
#             if node != '#':
#                 # stk.append([node, 0])
#                 stk.append(0)

#         return i == n-1 and not stk


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        preorderArr = preorder.split(',')
        n = len(preorderArr)

        for i in range(n):
            node = preorderArr[i]
            if slots == 0:
                    return False

            if node == '#':
                slots -= 1
            else:
                slots += 1

        return slots == 0


s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
