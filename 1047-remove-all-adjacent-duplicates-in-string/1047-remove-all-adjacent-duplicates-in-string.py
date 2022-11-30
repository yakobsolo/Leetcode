class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ""
        for i in s:
            if stack:
                if i == stack[-1]:
                    stack= stack[:-1]
                else:
                    stack = stack + i
            else:
                stack =stack + i
        return stack