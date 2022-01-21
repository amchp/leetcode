class Solution:
    #There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].    
    #You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
    # Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
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