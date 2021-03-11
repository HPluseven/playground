class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stk = []
        num = 0
        preSign = '+'

        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = 10 * num + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stk.append(num)
                if preSign == '-':
                    stk.append(-num)
                if preSign == '*':
                    stk.append(stk.pop() * num)
                if preSign == '/':
                    stk.append(int(stk.pop() / num))
                preSign = s[i]
                num = 0

        return sum(stk)


s = Solution()
print(s.calculate("14-3/2"))
