class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        group_len = 0
        n = len(grades)
        i = 0
        while i< n:
            if n-i < group_len+1: return group_len
            
            group_len+=1
            i+=group_len
        return group_len
        