class Solution:
    #This problem was intereting because it was basically finding the first part of the loop that was positive and for the rest of the array stayed positive. It was an answer I had to see a few hidden test cases to understand but it was interesting.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rT = 0
        cT = 0
        ind = 0
        for i in range(len(gas)):
            rT += gas[i] - cost[i]
            cT += gas[i] - cost[i] 
            if cT < 0:
                ind = -1
                cT = 0
            if ind == -1 and gas[i] - cost[i] > 0:
                ind = i
        if rT < 0:
            return -1
        return ind