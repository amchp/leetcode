class Solution:
    #This problem was just see that there weren't taht many stations so it was easier to crete a map of station and keep measuring the capacity
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[1])
        leave = [0] * 1001
        c = 0
        stops = []
        for p, f, t in trips:
            leave[f] += p
            leave[t] -= p
        for x in leave:
            c += x
            if c > capacity:
                return False
        return True