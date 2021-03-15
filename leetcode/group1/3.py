# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLength = 0
#         for idx, char in enumerate(s):
#             sub_str = char
#             for i in range(idx + 1, len(s)):
#                 if s[i] not in sub_str:
#                     sub_str += s[i]
#                 else:
#                     break
#             maxLength = max(maxLength, len(sub_str))

#         return maxLength
