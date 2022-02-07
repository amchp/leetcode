class Solution:
    #It was another interesting divide the problem into parts that are manageable
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = defaultdict(int)
        for x in nums1:
            for y in nums2:
                d[x + y] += 1
        ans = 0
        for x in nums3:
            for y in nums4:
                ans += d[-(x + y)]
        return ans