# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


from typing import List

# 1. Brute force solution O(n^2)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1):
                return [i, j]
        return []


# Solution with extra space with O(n) complexity
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass


