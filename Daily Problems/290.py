class Solution:
    #This was a dumb matching problem that you used a simple map to solve
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        m = [""] * 26
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if m[ord(pattern[i]) - ord('a')] != "":
                if s[i] == m[ord(pattern[i]) - ord('a')]:
                    continue
                return False
            else:
                m[ord(pattern[i]) - ord('a')] = s[i]
        for i in range(len(m)):
            for j in range(len(m)):
                if i != j and m[i] != "" and m[i] == m[j]:
                    return False
        return True