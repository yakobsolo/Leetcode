class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        N = len(cards)
        
        hash = {}
        
        mn = N+1
        
        for i in range(N):
            if cards[i] not in hash:
                hash[cards[i]] = i
            else:
                if i-hash[cards[i]] < mn:
                    mn = i-hash[cards[i]]
                hash[cards[i]] = i
        if mn == N+1:return -1
        return mn+1