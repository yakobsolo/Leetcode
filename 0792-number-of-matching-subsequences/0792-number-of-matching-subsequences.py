class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dic = defaultdict(list)
        
        for i in range(len(s)):
            dic[s[i]].append(i)
        
        ans = 0
        
        for word in words:
            cur = -1
            is_sub = True
            
            for let in word:
                index = bisect_right(dic[let],cur)
                
                if index == len(dic[let]):
                    is_sub = False
                    break
                
                cur = dic[let][index]
            if is_sub:
                ans += 1
        return ans