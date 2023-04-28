class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = collections.deque()
        q.append(["0","0","0","0"])
        visted = set()
        turn = 1
        if target == "0000": return 0
        if "0000" in deadends: return -1
        while q:
            
            q_len = len(q)
            flag = 0
            
            for _ in range(q_len):
                
                comb = q.popleft()
                for i in range(4):
                    comb1, comb2 = comb.copy(), comb.copy()

                    # print(i)
                    # if int(comb[i]) +1 > 9 or int(comb[i]) -1 < -1: continue
                    
                    comb1[i] = str((int(comb[i]) +1)%10)
                    temp1 = "".join(comb1)
                    
                    if temp1 not in visted:
                        visted.add(temp1)
                        if temp1 == target: 
                            return turn
                        if temp1 not in deadends:
                            q.append(comb1)
                    # print(q)

                        
                    # comb2
                    idx = int(comb[i]) -1
                    if idx == -1:
                        idx = 9
                    comb2[i] = str(idx)
                    temp2 = "".join(comb2)
                    if temp2 not in visted:
                        visted.add(temp2)
                        if temp2 == target: 
                            return turn
                            
                        if temp2 not in deadends:
                            q.append(comb2)
                        
                    # print(q)
                        
        
            
            
            turn +=1
        
        return -1
                