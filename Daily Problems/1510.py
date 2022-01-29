class Solution:
    #This was a min max that was toughto implement there was a better dp solution but tough to implement
    def minMax(self, n, turn):
        if self.dp[turn][n] != None:
            return self.dp[turn][n]
        optimal = None
        for x in range(1, int(sqrt(n)) + 1):
            if self.minMax(n - x*x, not turn) == turn:
                optimal = turn
                break
            else:
                optimal = not turn
        self.dp[turn][n] = optimal
        return optimal
    
    def winnerSquareGame(self, n: int) -> bool:
        self.dp = [[None] * (n+1) for i in range(2)]
        self.dp[0][0], self.dp[1][0] = True, False 
        self.minMax(n, 1)
        return self.dp[1][n]