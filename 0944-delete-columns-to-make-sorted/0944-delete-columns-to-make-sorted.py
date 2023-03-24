class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        hashmap = defaultdict(list)
        count = 0
        for i in range(len(strs)):
            strg = strs[i]
            for j in range(len(strg)):
                hashmap[j].append(strg[j])
            
    
        for key in hashmap:
            values = hashmap[key]
            for i in range(1, len(values)):
                if values[i] < values[i-1]:
                    count+=1
                    break
        
        return count
            