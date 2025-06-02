class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                st.append(i)
            else:
                if len(st) != 0:
                    if i == ')' and st[-1] == '(' or i == '}' and st[-1] == '{' or i == ']' and st[-1] == '[':
                        st.pop()
                    else:
                        return False
                else:
                    return False
        if len(st) == 0:
            return True
        else:
            return False

                