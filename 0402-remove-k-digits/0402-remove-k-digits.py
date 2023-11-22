class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return "0"
        
        stack = []
        for n in num:
            while k>0 and stack and int(stack[-1])>int(n):
                stack.pop()
                k-=1
            stack.append(n)
        while k>0:
            stack.pop()
            k-=1
        ans = "".join(stack).lstrip("0")
        return ans if ans else "0"
            