class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n
        for i in range(n):
            count = 0
            for j in range(n):
                if boxes[j] == "1":
                    count += abs(j-i)
            res[i] = count
        return res