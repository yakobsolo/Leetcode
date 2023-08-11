class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        heap = []
        word_count = Counter(words)
        for word in word_count:
            heapq.heappush(heap, (-word_count[word], word))
        ans = []
        while k:
            ans.append(heappop(heap)[1])
            k-=1
        return ans