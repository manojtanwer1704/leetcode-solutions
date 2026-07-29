# LeetCode 15 - 3Sum
# Approach: Sorting + Two Pointers
# Time Complexity: O(n²)
# Space Complexity: O(1)  # (excluding the output list)

class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        result = []
        for i in range(0,n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            target = -nums[i]
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:

                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif current_sum < target:
                    left+=1
                else:
                    right-=1
        return result
