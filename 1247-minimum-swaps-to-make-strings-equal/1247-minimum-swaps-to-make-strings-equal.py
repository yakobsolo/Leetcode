class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy += 1
            elif c1 == 'y' and c2 == 'x':
                yx += 1
        
        if (xy + yx) % 2:
            return -1
        
        return xy // 2 + yx // 2 + (yx % 2) * 2