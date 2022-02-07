class Solution:
    #It is an interesting problem that first you have to find the size and then change the list
    def removeDuplicates(self, nums: List[int]) -> int:
        second = True
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                second = True
                k += 1
            elif second:
                second = False
                k += 1
        i = 1
        j = 1
        p = nums[0]
        second = True
        while j < k and i < len(nums):
            if nums[i] != p:
                p = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
                second = True
                j += 1
            elif second:
                nums[i], nums[j] = nums[j], nums[i]
                second = False
                j += 1
            i += 1
        return k