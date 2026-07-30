# 27. Remove Element

- **Language:** Python 3
- **Data Structure:** Array
- **Topic:** In-place Array Modification
- **Time Complexity:** O(N²) — Due to `pop(i)` shifting elements
- **Space Complexity:** O(1) — In-place modification

## Solution Code

```python
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
