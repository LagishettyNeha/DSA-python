class Solution:
    def kthCharacter(self, k: int) -> str:
        def next_character(c):
            return chr(((ord(c)-ord('a')+1) % 26)+ord('a'))
        word = "a"
        while len(word) < k:
            next_part = ''.join(next_character(c) for c in word)
            word += next_part
        return word[k-1]
