class Solution:
    #It was an interesting dictionary problem
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        d = [0] * 26
        for x in p:
            d[ord(x) - ord('a')] += 1
        ans = []
        for i in range(len(p) - 1):
            d[ord(s[i]) - ord('a')] -= 1
        i = 0
        j = len(p) - 1
        while j < len(s):
            d[ord(s[j]) - ord('a')] -= 1
            pas = True
            for x in d:
                if x:
                    pas = False
                    break
            if pas:
                ans.append(i)
            d[ord(s[i]) - ord('a')] += 1
            i += 1
            j += 1
        return ans