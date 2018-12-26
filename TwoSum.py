import itertools
import numpy as np


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Memory Exceeded
        # sub_nums = list(filter(lambda x: x[0] + x[1] == target, list(set(itertools.combinations(nums, 2)))))

        # for (a, b) in sub_nums:
        #     if a+b == target:
        #         if a != b:
        #             return [nums.index(a), nums.index(b)]
        #         else:
        #             indices = [i for i, x in enumerate(nums) if x == a]
        # return [indices[0], indices[1]]

        # # Time out
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        for num in nums:
            value = target - num

            if value == num:
                if nums.count(value) >= 2:
                    indices = [i for i, x in enumerate(nums) if x == value]
                    return [indices[0], indices[1]]
            else:
                if value in nums:
                    return [nums.index(num), nums.index(value)]
