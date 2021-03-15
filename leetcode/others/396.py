import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_str_lens = []

        def divide(s):
            counter = collections.Counter(s)
            splits = []
            for ch, num in counter.most_common():
                if num < k:
                    splits.append(ch)

            if not splits:
                max_str_lens.append(len(s))
                return

            for split in splits:
                s = s.replace(split, '$')
            strs = [item for item in s.split('$') if item]
            for str_ in strs:
                divide(str_)
        divide(s)
        return max(max_str_lens) if max_str_lens else 0


s = Solution()
print(s.longestSubstring("aaabb", 3))
