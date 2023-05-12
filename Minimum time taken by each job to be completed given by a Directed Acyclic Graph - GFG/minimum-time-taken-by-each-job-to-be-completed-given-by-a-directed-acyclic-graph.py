from typing import List


from typing import List
import collections

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph=collections.defaultdict(list)
        indegree=[0] * (n+1)
        
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        q=collections.deque()
        for i in range(1,n+1):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        lev=1
        
        ans = [0]*n
        while q:
            q_len=len(q)
            for _ in range(q_len):
                
                top=q.popleft()
                ans[top-1] = lev
                for adj in graph[top]:
                    indegree[adj]-=1
                    if indegree[adj]==0:
                        q.append(adj)
            lev+=1
            
        
        
        return " ".join(map(str,ans))
            

                    


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends