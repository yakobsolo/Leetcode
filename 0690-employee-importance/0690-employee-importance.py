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
        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id] = employee.subordinates
            graph[employee.id].append(employee.importance)
        
        def dfs(empId):
            # print(graph)
    
            tot = 0
            for i in range(len(graph[empId]) -1):
                tot+= dfs(graph[empId][i])
            # print(graph[empId])
            tot += graph[empId][-1]
            return tot
        return dfs(id)
                
                
            
        
        
    