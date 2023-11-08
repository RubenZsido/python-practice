class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        cx = sx
        cy = sy
        for i in range(t):
            if cx == fx and cy == fy:
                return True
            dirX, dirY = normalizeNum(fx - cx), normalizeNum(fy - cy)
            cx += dirX
            cy += dirY
        return False
def normalizeNum(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0