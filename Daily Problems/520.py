class Solution:
    #This was an easy follow the instruction question
    def detectCapitalUse(self, word: str) -> bool:
        c = 0
        for x in word:
            if x.isupper():
                c += 1
        return c == 0 or (word[0].isupper() and c == 1) or c == len(word)