class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count =0
        n = len(words)
        
        sets = [set(word) for word in words]
        for i in range(n):
            for j in range(i+1, n):
                if sets[j] == sets[i]:
                    count +=1
        return count
                