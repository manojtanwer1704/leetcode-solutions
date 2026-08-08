# 142. Linked List Cycle II

- **Language:** Python 3
- **Data Structure:** Singly Linked List
- **Algorithm:** Floyd's Cycle Detection (Phase 1 & Phase 2)
- **Time Complexity:** O(N) — Linear time traversal
- **Space Complexity:** O(1) — Constant memory space

## Key Takeaway
1. **Phase 1:** Use fast and slow pointers to detect if a cycle exists.
2. **Phase 2:** Once they meet, reset `slow` to `head`. Move both pointers 1 step at a time. Mathematically, the point where they meet again is the start node of the cycle.

## Solution Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head 
        fast = head
        
        # Phase 1: Detect Cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            # Cycle detected
            if slow == fast:
                # Phase 2: Find Entry Point
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Start node of cycle
                
        return None  # No cycle found
