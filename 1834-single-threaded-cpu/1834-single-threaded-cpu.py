class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        for i, task in enumerate(tasks):
            task.append(i)
            
        tasks.sort()
        
        ans , heap = [], []
        t = 0
        i = 0
        
        
        while heap or i< len(tasks):
            while i<len(tasks) and t >= tasks[i][0]:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                
                i+=1
            
            if not heap:
                t = tasks[i][0]
            else:
                p, idx = heapq.heappop(heap)
                ans.append(idx)
                t +=p
        return ans