class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if sx == fx and sy == fy and t == 1:
            return False
        diffX, diffY = abs(fx - sx), abs(fy - sy)
        if diffX > diffY:
            diffX = diffX - diffY
        else:
            diffY = diffY - diffX
        distance = diffX + diffY
        if t >= distance:
            return True
        return False