class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        N = len(cards)
        
        count = defaultdict(list)
        
        for i in range(N):
            count[cards[i]].append(i)
        
        mn  = inf
        for key , values in count.items():
            for i in range(1, len(values)):
                mn = min(mn, values[i]-values[i-1])
        return mn+1 if mn != inf else -1
                