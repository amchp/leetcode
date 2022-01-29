class Solution:
    #This was an interesting problem that could be easily done with a left distance and right distance vector
    def maxDistToClosest(self, seats: List[int]) -> int:
        lD = [0] * len(seats)
        rD = [0] * len(seats)
        dL = float('inf')
        dR = float('inf')
        for i in range(len(seats)):
            l = i
            r = len(seats) - 1 - i
            if seats[l] == 1:
                dL = -1
            if seats[r] == 1:
                dR = -1
            dL += 1
            dR += 1
            lD[l] = dL
            rD[r] = dR
        ans = 0
        for i in range(len(lD)):
            ans = max(ans, min(lD[i], rD[i]))
        return ans