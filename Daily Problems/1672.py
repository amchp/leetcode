class Solution:
    #Easy do what they are telling you to do question
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = 0
        for x in accounts:
            m = max(m, sum(x))
        return m