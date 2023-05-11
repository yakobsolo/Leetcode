class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0, 1, 0))
        
        def bfs():
            while q:
                p, s, n = q.popleft()
                if p == target: return n

                q.append((p+s, s*2, n+1))
                if s>0:
                    if p+s>target: q.append((p, -1, n+1))
                else:
                    if p+s<target: q.append((p, 1, n+1))
                    
        return bfs()
        