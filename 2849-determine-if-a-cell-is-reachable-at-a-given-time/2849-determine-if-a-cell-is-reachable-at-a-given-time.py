class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy and t==1: return False
        count_y = abs(fy-sy)
        count_x = max(count_y, abs(fx - sx))
        if t< count_x:return False
        return True