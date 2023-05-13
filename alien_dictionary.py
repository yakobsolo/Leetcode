#User function Template for python3
import collections
class Solution:
    def findOrder(self,alien_dict, N, K):

    # code here
    
        isedge = []
        for i in range(k):
            row = []
            for j in range(k):
                row.append(False)
            isedge.append(row)
        
        for i in range(len(alien_dict) -1):
            w1, w2 = alien_dict[i], alien_dict[i+1]
            minleng= min(len(w2), len(w1))
            for j in range(minleng):
                if w1[j] != w2[j]:
                    isedge[ord(w1[j]) - 97][ord(w2[j]) - 97] = True
                    break
        
        graph = collections.defaultdict(list)
        for i in range(k):
            for j in range(k):
                if isedge[i][j]:
                    graph[i].append(j)
                    
        
        res = []
        visted = [False] * k
        
        def dfs(i):
            visted[i] = True
            for adj in graph[i]:
                if not visted[adj]:
                    dfs(adj)
            res.append(i)
            
        for i in range(k):
            if not visted[i]: dfs(i)
        
        ans = ""
        while res:
            i = res.pop()
            ans += chr(i + 97)
        return ans
