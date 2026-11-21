class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token not in "+-*/":
                st.append(int(token))

            else:
                n1 = st.pop()
                n2 = st.pop()
                res = 0

                match token:
                    case '+':
                        res = n2 + n1
                    case '-':
                        res = n2 - n1
                    case '/':
                        res = int(n2 / n1)
                    case '*':
                        res = n2 * n1
                st.append(res)
        return st[-1]
