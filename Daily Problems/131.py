class Solution:
    #This was an interesting problem basically what I did was find all the internal palindrome and then I connected all possible palindromes to get my answer
    def partition(self, s: str) -> List[List[str]]:
        def dfs(p, ans, c, s, i):
            if i >= len(p):
                ans.append(c.copy())
                return
            for i, j in p[i]:
                c.append(s[i:j])
                dfs(p, ans, c, s, j)
                c.pop()
        p = [[] for _ in s]
        for i in range(len(s)):
            for j in range(i + 1,len(s) + 1):
                c = s[i:j]
                if c == c[::-1]:
                    p[i].append((i,j))
        ans = []
        c = []
        dfs(p, ans, c, s, 0)
        return ans