class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)
        dq = deque([N - 1])
        for i in range(N - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                dq.appendleft(i)
            elif arr[i] == arr[i + 1]:
                dq[0] = i
            else:
                while arr[dq[-1]] >= arr[i]:
                    dq.pop()
                arr[i], arr[dq[-1]] = arr[dq[-1]], arr[i]
                break
        return arr