class MedianFinder:
    import heapq
    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if self.left and self.right and -self.left[0] > self.right[0]:
                val = -heapq.heappop(self.left)
                heapq.heappush(self.right, val)
        if len(self.left) > len(self.right) + 1:
            max = -heapq.heappop(self.left)
            heapq.heappush(self.right, max)
        if len(self.right) > len(self.left) + 1:
            min = -heapq.heappop(self.right)
            heapq.heappush(self.left, min)
            
        
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]
        return (-self.left[0] + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()