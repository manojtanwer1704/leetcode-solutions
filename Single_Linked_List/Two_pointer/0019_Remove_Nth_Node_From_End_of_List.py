# 19. Remove Nth Node From End of List

- **Language:** Python 3
- **Data Structure:** Singly Linked List
- **Algorithm:** Two Pointers (Fast & Slow / Runner Technique)
- **Time Complexity:** O(L) — Single pass traversal where L is total nodes
- **Space Complexity:** O(1) — Constant extra space (In-place modification)

## Key Takeaway
By advancing the `fast` pointer $n$ steps ahead first, we create a constant gap of $n$ nodes between `fast` and `slow`. When `fast` reaches the end, `slow` naturally points to the node right before the target node to be deleted.

## Solution Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        
        # Advance fast pointer by n steps
        for _ in range(n):
            fast = fast.next
            
        # Edge Case: If fast reaches None, remove the head node
        if fast is None:
            return head.next
            
        # Move both pointers until fast reaches the last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        # Delete the N-th node from end
        slow.next = slow.next.next
        
        return head
