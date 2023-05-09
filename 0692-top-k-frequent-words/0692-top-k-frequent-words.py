class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.defaultdict(int)
        
        for word in words:
            count[word] -=1
            
        heap = [(v, k) for k, v in count.items()]
        heapq.heapify(heap)
        
        ans = []
        while k:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans