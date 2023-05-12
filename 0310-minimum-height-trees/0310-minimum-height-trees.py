class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph=defaultdict(list)
        indegree = [0] *n 
        for p, c in edges:
            graph[p].append(c)
            graph[c].append(p)
            indegree[p] +=1
            indegree[c] +=1
        
        q = deque()
        for i in range(n):
            if indegree[i] <= 1: q.append(i)
         
        ans = []
        while q:
            temp = []
            q_len =len(q)

            for _ in range(q_len):

                top = q.popleft()
                temp.append(top)

                for adj in graph[top]:
                    indegree[adj] -=1
                    if indegree[adj] == 1:
                        q.append(adj)

            ans = temp

        return ans