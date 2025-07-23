class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        if x < y:
            return self.maximumGain(s[::-1], y, x)
        st1 = []
        for c in s:
            if c != 'b':
                st1.append(c)
            else:
                if st1 and st1[-1] == 'a':
                    st1.pop()
                    ans += x
                else:
                    st1.append(c)
        st2 = []
        while st1:
            ch = st1.pop()
            if ch != 'b':
                st2.append(ch)
            else:
                if st2 and st2[-1] == 'a':
                    st2.pop()
                    ans += y
                else:
                    st2.append(ch)
        return ans
