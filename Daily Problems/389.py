class Solution:
    #Febuary seems to be the month of the dictionary
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = [0] * 26
        d2 = [0] * 26
        for x in s:
            d1[ord(x) - ord('a')] += 1
        for x in t:
            d2[ord(x) - ord('a')] += 1
        for i in range(len(d1)):
            if d1[i] != d2[i]:
                return chr(ord('a') + i)
        return '?'