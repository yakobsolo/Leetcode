class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        incoming = [0]*numCourses
        q = deque()
        
        for c, p in prerequisites:
            graph[p].append(c)
            incoming[c] +=1
        
       # [0, 0]
        # []
        for i in range(len(incoming)):
            if incoming[i] == 0:
                q.append(i)
    
        order = []
        while q:
            top = q.popleft()
            order.append(top)
            
            for course in graph[top]:
                incoming[course] -=1
                
                if incoming[course] == 0:
                    q.append(course)
                    
            
            
        if len(order) != numCourses:
            return False
        return True
        