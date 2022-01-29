class Solution:
    #This was an annoying implementation problem
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        s = list(str(low))
        i = 1
        while int("".join(s)) <= high:
            if i == len(s):
                a = int("".join(s))
                if low <= a and a <= high:
                    ans.append(a)
                s[0] = str(int(s[0]) + 1)
                i = 1
            if int(s[i]) != int(s[i - 1]) + 1:
                s[i] = str(int(s[i - 1]) + 1)
                if int(s[i]) > 9:
                    if int(s[i - 1]) == 9:
                        s = list("1" * (len(s) + 1))
                        i = 0
                    else:
                        s[0] = str(int(s[0]) + 1)
                        i = 0
            i += 1
        return ans