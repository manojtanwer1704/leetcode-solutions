"""
LeetCode 1 - Two Sum

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [i,seen[remaining]]
            seen[nums[i]] = i
