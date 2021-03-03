class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []

        for n in range(num+1):
            count = 0
            while n:
                count += 1
                n = n & (n-1)
            ans.append(count)

        return ans

# dp


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        highBit = 0

        for n in range(1, num+1):
            if n & (n-1) == 0:
                highBit = n
            ans.append(ans[n - highBit] + 1)

        return ans
