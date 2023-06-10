class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        leng = len(board)
        def cell(n):
            r, c= (n-1)//leng, (n-1)%leng
            if r%2: c = leng-1-c
            return [r, c]
        
        q = collections.deque()
        q.append([1, 0])
        visted = set()
        board.reverse()
        while q:
            n, count = q.popleft()
            for i in range(1 , 7):
                nn = n+ i
                r, c = cell(nn)
                if board[r][c] != -1:
                    nn = board[r][c]
                
                if nn == leng**2: return count+1
                if nn not in visted:
                    visted.add(nn)
                    q.append([nn, count+1])
        return -1
                
            
        