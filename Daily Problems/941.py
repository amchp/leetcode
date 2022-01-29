class Solution:
    #This was an easy follow the instruction problem bu a little complicated to implement
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peak = -1
        if arr[0] > arr[1]:
            return False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if peak == -1 and arr[i] < arr[i - 1]:
                peak = i - 1
            elif peak != -1 and arr[i] > arr[i - 1]:
                return False
        return peak != -1