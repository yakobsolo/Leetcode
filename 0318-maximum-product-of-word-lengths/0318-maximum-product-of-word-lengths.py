class Solution:
    def maxProduct(self, words: List[str]) -> int:
        store = []
        
        leng= len(words)
        for i in range(leng):
            binary = 0
            for j in range(len(words[i])):
                binary |= (1<<(ord(words[i][j]) - 97))
                
            store.append(binary)
        ans = 0
        for i in range(len(store)):
            for j in range(i, len(store)):
                
                if store[i] & store[j] == 0:
                    ans  = max(ans, (len(words[i] * len(words[j]))))
        return ans
                

        
        