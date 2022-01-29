class Solution:
    #This problem was interesting because I thought it was greedy but I thought about it a lot and found that it was a binary search
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 0
        r = piles[-1]
        while l + 1 < r:
            m = (r - l) // 2 + l
            hours = 0
            for x in piles:
                hours += ceil(x / m)
            if hours <= h:
                r = m
            else:
                l = m
        return r