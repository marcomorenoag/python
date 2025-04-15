from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            if not nums or len(nums) < k:
                return res

            avg_value = target // k

            if nums[0] > avg_value or nums[-1] < avg_value:
                return res

            # Base case
            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for subset in kSum(nums[i + 1 :], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (
                    hi < len(nums) - 1 and nums[hi] == nums[hi + 1]
                ):
                    hi -= 1
                else:
                    res.append(nums[lo], nums[hi])
                    lo += 1
                    hi -= 1

            return res

        nums.sort()
        return kSum(nums, target, 4)


"""
[-2,-1,0,0,1,2]
target = 0
* -2 + 3Sum:
    target = 2
    * -1 + 2Sum:
        target = 3
        [[-1,1,2]]
    * 0 + 2Sum:
        target = 2
        [[0,0,2]]
    [[-2,-1,1,2],[-2,0,0,2]]
* -1 + 3Sum:
    target = 1
    * 0 + 2Sum:
        target = 1
        [[0,0,1]]
"""
