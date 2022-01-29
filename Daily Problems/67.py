class Solution:
    #I thought this problem was dumb so I just used the build in methods
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")
        