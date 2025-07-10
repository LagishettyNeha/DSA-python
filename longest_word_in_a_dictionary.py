class Solution:
    def longestWord(self, words: List[str]) -> str:
        hm = {}
        for i in words:
            hm[i] = 1
        ans = ""
        for i in words:
            if isPrefix(i, hm):
                if len(i) > len(ans):
                    ans = i
                elif len(i) == len(ans):
                    ans = min(ans, i)
        return ans


def isPrefix(word, hm):
    l = []
    for i in range(len(word)):
        l.append(word[:i+1])
    for i in l:
        if i not in hm:
            return False
    return True
