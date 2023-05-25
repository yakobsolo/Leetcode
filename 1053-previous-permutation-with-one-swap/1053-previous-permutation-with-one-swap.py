class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        q = deque([n-1])
        
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                q.appendleft(i)
            elif arr[i] == arr[i+1]:
                q[0] = i
            else:
                while arr[i] <= arr[q[-1]]:
                    q.pop()
                arr[i], arr[q[-1]] = arr[q[-1]], arr[i]
                break
        return arr