class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n<10: return -1
        
        stack = deque()
        n = str(n)
        for i in range(len(n) -1, -1, -1):
            if stack and int(stack[-1]) > int(n[i]):
                temp = stack.copy()
                temp.append(n[i])
                
                for j in range(len(temp)-1):
                    if int(temp[-1])<int(temp[j]):
                        temp[-1], temp[j] = temp[j], temp[-1]
                        break
                
                break
            stack.append(n[i])
        if len(stack) == len(n): return -1
        ans = ""
        ans += n[:i] + temp[-1] + "".join(temp)
        return int(ans[:-1]) if n != ans[:-1] and int(ans[:-1]) <= 2**31 -1 else -1