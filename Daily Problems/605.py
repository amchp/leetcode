class Solution:
    #This was a simple follow the instruction problem
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        for i in range(len(flowerbed)):
            l = True
            r = True
            if flowerbed[i] == 1:
                continue
            if i != 0:
                l = flowerbed[i - 1] == 0
            if i != len(flowerbed) - 1:
                r = flowerbed[i + 1] == 0
            if l and r:
                planted += 1
                flowerbed[i] = 1
        return planted >= n