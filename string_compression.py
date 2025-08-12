class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0
        i = 0
        ans = []
        while i < len(chars):
            ch = chars[i]
            count = 0
            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1
            chars[j] = ch
            j += 1
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
        return j
