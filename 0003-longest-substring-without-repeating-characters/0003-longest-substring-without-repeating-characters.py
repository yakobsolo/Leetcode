class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        long = 0
        max_long = 0
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
                long = len(stack)
                max_long = max(long, max_long)
            else:
                stack = stack[stack.index(s[i]):]
                stack.remove(s[i])
                stack.append(s[i])
        return max_long