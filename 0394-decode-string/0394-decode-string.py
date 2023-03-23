class Solution:
    def decodeString(self, s: str) -> str:
        stack  = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                
                string = ""
                
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                
                k = ''
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                stack += string*int(k)
                
        return "".join(stack)
    