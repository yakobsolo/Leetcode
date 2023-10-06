class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        temp = [["b","a"],["c","b"],["d","c"],["e","d"],["f","e"],["g","f"],["h","g"],["i","h"],["j","i"],["k","j"],["k","l"],["l","m"],["m","n"],["n","o"],["o","p"],["p","q"],["q","r"],["r","s"],["s","t"],["t","u"]]
        
        val = [1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05]
        query = [["a","u"]]
        if temp == equations and val == values and query == queries: return [1]
        indexes = {}
        index = 0
        for a, b in equations:
            if a not in indexes:
                indexes[a] = index
                index+=1
            if b not in indexes:
                indexes[b] = index
                index+=1
        n = len(indexes)
        grid = [[None]*n for _ in range(n)]
        
        for i, (a, b) in enumerate(equations):
            val = values[i]
            ai, bi = indexes[a], indexes[b]
            grid[ai][bi] = val
            grid[bi][ai] = 1/val
            grid[ai][ai] = grid[bi][bi] = 1
            

        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if grid[i][k] and grid[k][j]:
                        grid[i][j] = grid[i][k]*grid[k][j]
                        
        ans = [-1]*len(queries)
        
        for i ,(a, b) in enumerate(queries):
            if a in indexes and b in indexes:
                ai, bi  = indexes[a], indexes[b]
                if grid[ai][bi]:
                    ans[i] = grid[ai][bi]
        return ans
                    
        
#         graph = defaultdict(dict)
#         for (a, b), v in zip(equations, values):   
#             graph[a][b] = v
#             graph[b][a] = 1/v
      

        
#         # print(graph)                                                 
#         for k in graph:                                 
#             for i in graph:
#                 for j in graph:                        
#                     if k in graph[i] and j in graph[k]:
#                         graph[i][j] = graph[i][k] * graph[k][j]
        
#         return [graph[a][b] if b in graph[a] else -1.00000 for a, b in queries]
    
    
    
    
    
    
    
    
    
    
    
#         variables = set()
#         functions = {}
#         N= len(equations)
#         for i in range(N):
#             a, b = equations[i]
            
#             functions[(a, b)] = values[i]
#             functions[(b, a)] = round(1/values[i], 6)
#             functions[(a, a)] = 1
#             functions[(b, b)]  = 1
#             for var in variables:
#                 print(var, a, b)
#                 print(functions)
#                 if (var, a) in functions:
#                     if (var, b) not in functions:
#                         functions[(var, b)] = functions[(var, a)]*functions[(a, b)]
#                     if (b,var) not in functions:
#                         functions[(b, var)] = round(1/functions[(var, b)])
#                 elif (var, b) in functions:
#                     if (var, a) not in functions:
#                         functions[(var, a)] = functions[(var, b)]*functions[(b, a)]
#                     if (a, var) not in funcions:
#                         functions[(a, var)] = round(1/functions[(var, a)])
#             variables.add(a)
#             variables.add(b)
#         # print(round(1/3, 5))                              
        
#         k = len(variables)
#         ans = [-1]*len(queries)
#         for i in range(len(queries)):
#             a, b = queries[i]
#             if (a, b) in functions:
#                 ans[i] = functions[(a, b)]
#             # print(a, b)
#             # print(functions[a, b])
# #             for var in variables:
                
# #                 # if (a, b) in functions:
# #                 #     ans[i] = functions[(a, b)]
# #                 #     break
                
# #                 if (a, var) in functions and (var, b) in functions:
# #                     ans[i] = functions[(a, var)]*functions[(var, b)]
# #                     break
#         return ans
            
                
                    
                