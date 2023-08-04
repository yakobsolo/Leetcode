class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for n in hours:
            if n>= target:
                count +=1
        return count