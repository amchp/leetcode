class Solution:
    #This was a greedy sort solution but it was hard to think up
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[0])
        i = 0
        j = 1
        m = points[i][1]
        ans = 0
        while j < len(points):
            if m < points[j][0]:
                ans += 1
                i = j
                j = i + 1
                m = points[i][1]
                continue
            m = min(m, points[j][1])
            j += 1
        if i != len(points):
            ans += 1
        return ans