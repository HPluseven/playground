class Solution:
    def checkRecord(self, s: str) -> bool:
        numA = 0
        numL = 0

        for char in s:
            if numA > 1:
                return False
            if numL > 2:
                return False
            if char == 'P':
                numL = 0
                continue
            if char == 'A':
                numL = 0
                numA += 1
            if char == "L":
                numL += 1
        return numL < 3 and numA < 2
