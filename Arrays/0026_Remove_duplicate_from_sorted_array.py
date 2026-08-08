# 26. Remove Duplicates from Sorted Array

- **Language:** Python 3
- **Data Structure:** Array
- **Algorithm:** Two Pointers (In-place)
- **Time Complexity:** O(N) — Single pass through the array
- **Space Complexity:** O(1) — Constant space, modified array in-place

## Key Takeaway
Since the array is already sorted, duplicate elements will always be adjacent. We use a slow pointer `i` to keep track of the last unique element found and a fast pointer `j` to scan through the array.

## Solution Code

```python
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
            
        i = 0  # Slow pointer for unique element boundary
        
        # Fast pointer 'j' scans the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1
