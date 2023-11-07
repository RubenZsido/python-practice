class Solution(object):
    def twoSum(self, nums, target):
        for i, e in enumerate(nums):
            for i2, e in enumerate(nums):
                if not i2 == i:
                    sum = nums[i] + nums[i2]
                    if(sum == target):
                        print([i, i2])
                        return 
sol = Solution()
sol.twoSum([1,2,3], 5)
