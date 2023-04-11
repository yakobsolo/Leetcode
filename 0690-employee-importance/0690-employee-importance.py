"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinates = defaultdict(list)
        importance = {}
        
        for emp in employees:
            subordinates[emp.id] = emp.subordinates
            importance[emp.id] = emp.importance
        
        def impcalc(cur_id):
            tot = 0
            for sub in subordinates[cur_id]:
                tot += impcalc(sub)
            
            tot += importance[cur_id]
            return tot
        return impcalc(id)
        
        
        
    