class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        self.h = []
        for n in nums:
            if len(self.h) < k:
                heappush(self.h, n)
            elif n > self.h[0]:
                heappop(self.h)
                heappush(self.h, n)
                
        
        

    def add(self, val: int) -> int:
        if len(self.h) < self.k: heappush(self.h, val)
        else: heappushpop(self.h, val)
        return self.h[0]
            
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)