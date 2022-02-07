class Solution:
    #It is an easy do what they tell you to do
    #It had an interesting order to it
    def maxProfit(self, prices: List[int]) -> int:
        mi = float('inf')
        m = 0
        for x in prices:
            mi = min(mi, x)
            m = max(m, x - mi)
        return m