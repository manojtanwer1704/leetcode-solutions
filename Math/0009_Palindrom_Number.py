# 9. Palindrome Number

- **Language:** Python 3
- **Data Structure:** Math / Integers
- **Algorithm:** Number Reversal (Base-10 Arithmetic)
- **Time Complexity:** O(log₁₀(N)) — Proportional to the number of digits
- **Space Complexity:** O(1) — No string conversion, constant extra space

## Key Takeaway
Reversing the integer mathematically using modulo `% 10` and integer division `// 10` avoids converting the number to a string, making it memory-efficient. Negative numbers are automatically excluded since `-` cannot form a palindrome.

## Solution Code

```python
class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes (e.g., -121 != 121-)
        if x < 0:
            return False
            
        num = x
        rev = 0
        
        while num != 0:
            rev = rev * 10 + num % 10
            num //= 10
            
        return rev == x
