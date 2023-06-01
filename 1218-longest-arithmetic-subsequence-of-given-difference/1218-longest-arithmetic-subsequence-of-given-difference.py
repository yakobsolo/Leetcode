class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = {}
        visted = set()
        
        n = len(arr)
        for i in range(n):
            prev = arr[i] -difference
            if prev not in dic: dic[arr[i]] = 1
            else:
                if arr[i] in dic:    
                    dic[arr[i]] = max(dic[prev]+1, dic[arr[i]])
                else:
                    dic[arr[i]] = dic[prev] + 1
           
            
        maxx = 0
        for key in dic:
            maxx = max(maxx, dic[key])
        return maxx