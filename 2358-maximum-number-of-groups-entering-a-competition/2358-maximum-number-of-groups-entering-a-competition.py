class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        
        return int((-1 + sqrt(1+8*n))//2)
        