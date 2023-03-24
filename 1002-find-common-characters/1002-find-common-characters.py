class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        minlengword = min(words)
        ans = []
        hashmap = {}
        for i in range(len(words)):
            hashmap[i] = Counter(words[i])
            
        for c in minlengword:
            count = 0
            
            for i in hashmap:
                
                if c in hashmap[i]:
                    count+=1
                    hashmap[i][c] -=1
                    if hashmap[i][c] == 0:
                        del hashmap[i][c]
                
            if count == len(words):
                ans.append(c)
        return ans
            