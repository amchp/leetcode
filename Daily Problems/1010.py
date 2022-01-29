class Solution:
    #This problem was easy it was just making a dictionary and grouping the songs into classes and adding to answer the opposite class
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        dp = defaultdict(int)
        for t in time:
            ans += dp[(60 - t) % 60]
            dp[t % 60] += 1
        return ans