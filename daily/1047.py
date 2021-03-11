class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = []

        for char in S:
            if stk and char == stk[-1]:
                stk.pop()
            else:
                stk.append(char)

        return ''.join(stk)
