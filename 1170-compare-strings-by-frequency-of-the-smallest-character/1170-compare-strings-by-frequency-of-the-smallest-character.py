class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        lenquer = len(queries)
        lenword = len(words)
        
        query, word = [], []
        for i in range(lenquer):
            temp = Counter(queries[i])
            
            count = temp[sorted(temp)[0]]
            
            query.append(count)
        
        for j in range(lenword):
            temp = Counter(words[j])
            
            count = temp[sorted(temp)[0]]
            
            
            word.append(count)
        ans = []
        print(query, word)
        for q in query:
            count = 0
            for w in word:
                if w>q:
                    print(w)
                    count +=1
            ans.append(count)
        return ans
        
        
        
        