class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lookup = {}
        for idx, c in enumerate(s):
            lookup[c] = idx
        stack, seen = [], set()
        
        for i , c in enumerate(s):
            if c in seen: continue
            while stack and stack[-1] > c and lookup[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(c)
            seen.add(c)
        return "".join(stack)