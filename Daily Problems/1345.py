class Solution:
    #This was a tough problem that I had to call help from a friend to add that key del line to optimize the DP solution
    def minJumps(self, arr: List[int]) -> int:
        m = defaultdict(list)
        for i, x in enumerate(arr):
            m[x].append(i)
        q = deque()
        qq = deque()
        visited = [False] * len(arr)
        q.append(0)
        ans = 0
        while len(q) > 0:
            q, qq = qq, q
            while len(qq) > 0:
                i = qq.popleft()
                if visited[i]:
                    continue
                if i == len(arr) - 1:
                    return ans
                x = arr[i]
                visited[i] = True
                if i - 1 > -1 and not visited[i - 1]:
                    q.append(i - 1)
                if i + 1 < len(arr) and not visited[i + 1]:
                    q.append(i + 1)
                for j in m[x]:
                    if not visited[j]:
                        q.append(j)
                del(m[x])
            ans += 1
        return -1