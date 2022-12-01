class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i,1])
            if stack[-1][1] == k:
                stack.pop()
        return ''.join(c*n for c, n in stack)
#         same = 1
#         stack = []
#         for i in s:
#             if stack:
#                 if i == stack[-1]:
#                     same += 1
#                     stack.append(i)
#                     if same == k:
#                         while same:
#                             stack.pop()
#                             same -= 1
#                         same +=1
                    
#                 else:
#                     stack.append(i)
#             else:
#                 stack.append(i)
#         return ''.join(stack)
        