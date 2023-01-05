class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count =0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if set(words[j]) == set(words[i]):
                    count +=1
        return count
                