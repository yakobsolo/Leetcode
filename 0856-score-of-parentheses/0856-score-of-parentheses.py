class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        res, stack = 0, [0]
        for i in range(n):
            
            if s[i] == '(':
                stack.append(0)
            else:
                lastelem = stack.pop()
                
                if lastelem == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += lastelem * 2
        return stack[-1]
                    