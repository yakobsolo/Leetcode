class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key= len)
        
        
        n = len(words)
        dp = [1]*n
        print(sorted_words)
        for i in range(1, n):
            word = sorted_words[i]
            m = len(sorted_words[i])
            for j in range(i-1, -1, -1):
                
                if m == len(sorted_words[j])+1:
                    word2 = sorted_words[j]
                    for k in range(m):
                        temp = word[:k] + word[k+1:]
                        if temp == word2:
                            dp[i] = max(dp[i], dp[j]+1)
                            
                elif m > len(sorted_words[j]) +1: break
        return max(dp)
                