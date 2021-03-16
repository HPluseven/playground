class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        abs_num = abs(num)
        ans = []

        while abs_num:
            ans = [str(abs_num % 7)] + ans
            abs_num //= 7
        ret = ''.join(ans)
        return '-'+ret if num < 0 else ret
