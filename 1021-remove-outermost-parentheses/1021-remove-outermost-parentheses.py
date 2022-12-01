class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack= []
        res = []
        counter = 0
        for i in s:
            stack.append(i)
            if i == '(':
                counter += 1
            elif i == ')':
                counter -= 1
            if counter == 0:
                res += stack[1:-1]
                stack = []
        return "".join(res)
    