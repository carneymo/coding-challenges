# https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            if index == 0: continue
            nums[index] = nums[index-1] + nums[index]
        return nums


sol = Solution()
print(sol.runningSum([1,2,3,4]))
print(sol.runningSum([1,1,1,1,1]))
