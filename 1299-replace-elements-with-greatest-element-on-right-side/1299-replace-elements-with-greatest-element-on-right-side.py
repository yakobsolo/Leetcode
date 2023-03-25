class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        queue = deque()
        queue.appendleft(-1)
        for i in range(len(arr) -1, -1, -1):
            if arr[i] > queue[0]:
                queue.appendleft(arr[i])
            else:
                queue.appendleft(queue[0])
        for i in range(len(arr)):
            arr[i] = queue[i+1]
        return arr