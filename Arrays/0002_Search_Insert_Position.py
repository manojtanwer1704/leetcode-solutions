# LeetCode 35 - Search Insert Position
# Approach: Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums) and target >= nums[i]:
            if target == nums[i]:
                return i
            i += 1
        return i
