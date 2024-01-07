class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        i = 0
        stack = []
        for n in popped:
            if stack and stack[-1] == n:
                stack.pop()
                continue
            while i < N:
                if pushed[i] == n:
                    i+=1
                    break
                stack.append(pushed[i])
                i+=1
        if stack: return False
        return True
                    