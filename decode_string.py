class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in s:
            if i != ']':
                st.append(i)
            else:
                cur = ""
                while st[-1] != '[':
                    cur = st.pop()+cur
                st.pop()
                cur_num = ""
                while st and st[-1].isdigit():
                    cur_num = st.pop()+cur_num
                cur = int(cur_num)*cur
                st.append(cur)
        return "".join(st)
