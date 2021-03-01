class Solution:
    def judgeCircle(self, moves: str) -> bool:
        point = [0, 0]
        for move in moves:
            if move == 'U':
                point[1] += 1
            elif move == 'D':
                point[1] -= 1
            elif move == 'L':
                point[0] -= 1
            elif move == 'R':
                point[0] += 1
        if point[0] == 0 and point[1] == 0:
            return True
        return False
