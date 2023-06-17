class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n
        op, count = 0, 0
        for i in range(n):
            res[i] = op
            if boxes[i] == "1": count +=1
            op += count
        op , count = 0, 0
        for i in range(n-1, -1, -1):
            res[i] += op
            if boxes[i] == "1": count+=1
            op+= count
        return res