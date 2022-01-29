class Solution:
    #This was an interesting DP because you had to keep in mind both robots but after knowing that you just make 3D array to do this it becomes pretty easy
    def aux(self, grid, dp, i, j, k):
        if i == len(grid):
            return 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        op = [-1, 0, 1]
        m = 0
        if j == k:
            p = grid[i][j]
        else:
            p = grid[i][j] + grid[i][k]
        for x in op:
            if j + x < 0 or j + x >= len(grid[0]):
                continue
            for y in op:
                if k + y > -1 and k + y < len(grid[0]):
                    m = max(m, self.aux(grid, dp, i+1, j+x, k+y) + p)
        dp[i][j][k] = m
        return m
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = [[[-1]* len(x) for y in x] for x in grid]
        return self.aux(grid, dp, 0, 0, len(grid[0]) - 1)