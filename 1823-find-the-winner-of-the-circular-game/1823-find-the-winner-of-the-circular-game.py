class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        i =0 
        leng = len(arr)
        while len(arr) > 1:
            cur = i + k -1
            cur %= len(arr)
            arr.pop(cur)
            i = cur
        return arr[0]