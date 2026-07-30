# 328. Odd Even Linked List

- **Language:** Python 3
- **Data Structure:** Singly Linked List
- **Algorithm:** Multi-pointer Re-linking (In-place)
- **Time Complexity:** O(N) — Single pass through the linked list
- **Space Complexity:** O(1) — In-place rearrangement without extra memory

## Key Takeaway
We maintain separate pointers for odd and even nodes. By skipping nodes (`odd.next = odd.next.next`), we segregate odd and even indices simultaneously. Finally, we attach the head of the even list (`even_head`) at the end of the last odd node.

## Solution Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        # Base case: 0 or 1 node
        if head is None or head.next is None:
            return head
            
        odd = head
        even = head.next
        even_head = even
        
        # Link odd to odd, even to even
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            
            even.next = even.next.next
            even = even.next
            
        # Connect odd list's end with even list's head
        odd.next = even_head
        
        return head
