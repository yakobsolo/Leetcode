class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = Counter(s)
        valset = set()
        for i in hashmap:
            valset.add(hashmap[i])
        if len(valset) == 1:
            return True
        return False