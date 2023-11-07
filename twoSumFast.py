class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, cur in enumerate(nums):
            #target = curr + x
            #x = target - curr
            x = target - cur
            if cur in map:
                return [i, map[cur]]
            map[x] = i
sol = Solution()
ans = sol.twoSum([1,2,3], 5)
print(ans)
