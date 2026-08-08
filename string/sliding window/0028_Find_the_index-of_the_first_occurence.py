# 28. Find the Index of the First Occurrence in a String

- **Language:** Python 3
- **Data Structure:** String
- **Algorithm:** Sliding Window / Substring Matching
- **Time Complexity:** O(H × N) — Where H is length of haystack and N is length of needle
- **Space Complexity:** O(N) — Due to string slicing memory allocation in Python

## Key Takeaway
Slide a fixed window of size $N$ (length of `needle`) across `haystack` and check if the current slice matches `needle`. Return the starting index on first match, or `-1` if no match is found.

## Solution Code

```python
class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        n = len(needle)
        
        # Base edge case: exact match
        if haystack == needle:
            return 0
            
        # Slide window of size 'n' through haystack
        while i + n <= len(haystack):
            if haystack[i:i+n] == needle:
                return i
            else:
                i += 1
                
        return -1
