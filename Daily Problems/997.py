class Solution:
    #Another easy problem literally just check it there is a person that checks all the boxes with arrays
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p = [0] * (n + 1)
        t = [0] * (n + 1)
        for x, y in trust:
            p[x] += 1
            t[y] += 1
        for i in range(1, n+1):
            if p[i] == 0 and t[i] == n - 1:
                return i
        return -1