# 141. Linked List Cycle

- **Language:** Python 3
- **Data Structure:** Singly Linked List
- **Algorithm:** Floyd's Cycle Detection / Tortoise & Hare (Fast & Slow Pointers)
- **Time Complexity:** O(N) — Traverses at most N nodes
- **Space Complexity:** O(1) — Constant memory space

## Key Takeaway
We use two pointers moving at different speeds: `slow` moves 1 step, while `fast` moves 2 steps. If a cycle exists, the `fast` pointer will eventually catch up to the `slow` pointer inside the loop. If no cycle exists, `fast` will reach the end (`None`).

## Solution Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head 
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Fast caught up to slow -> Cycle detected
            if slow == fast:
                return True
                
        # Fast reached None -> No cycle
        return False
