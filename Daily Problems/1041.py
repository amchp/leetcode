class Solution:
    #This iteresting problem where you just had to check if it went in circles or it stayed at the start
    def isRobotBounded(self, instructions: str) -> bool:
        xD = 0
        yD = 0
        turns = 0
        for x in instructions:
            if x == "G":
                if turns == -1 or turns == 3:
                    xD += 1
                if turns == -3 or turns == 1:
                    xD -= 1
                if abs(turns) == 2:
                    yD -= 1
                if turns == 0:
                    yD += 1
            if x == 'L':
                turns += 1
            elif x== 'R':
                turns -= 1
            turns %= 4
        return (xD == 0 and yD == 0) or turns != 0