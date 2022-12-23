class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countchange = 0
        min_countchange = len(blocks)
        black = ""
        
        for i in range(len(blocks)):
            black += blocks[i]
            if blocks[i] == 'W':
                countchange +=1 
            if len(black) >= k:
                min_countchange = min(min_countchange, countchange)

                if black[0] =="W":
                    countchange -=1
                black = black[1:]
        return min_countchange
        
