class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = defaultdict(int)
        for v in arr: dic[v] = max(dic[v], dic[v - difference] + 1)
        return max(dic.values())
            
       