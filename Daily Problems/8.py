class Solution:
    #This problem was annoying to program I should have used regular expression but I didn't know what that was
    def myAtoi(self, s: str) -> int:
        nN = False
        negative = False
        n = 0
        for c in s:
            if  not nN and (c == '+' or c == '-'):
                nN = True
                if c == '-':
                    negative = True
            elif c.isdigit():
                nN = True
                n *= 10
                n += ord(c) - ord('0')
            elif not nN and c == ' ':
                continue
            else:
                break
        if negative:
            n *= -1
        if n < -(2 ** 31):
            return -(2 ** 31)
        if n > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return n