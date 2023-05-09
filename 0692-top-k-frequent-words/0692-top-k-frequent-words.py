class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.defaultdict(int)
        
        for word in words:
            count[word] -=1
        arr = [(v, k) for k, v in count.items()]
        
        heap = []
        for val in arr: 
            heapq.heappush(heap, val)
            
        ans = []
        print(heap)
        while k:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans