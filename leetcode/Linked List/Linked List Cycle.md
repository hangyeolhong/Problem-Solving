### Python solution
```python
#1. Hashset: O(n), O(n)
#2. Linked list with memory complexity O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False
```

### Explanation
- If there's a cycle, ```fast``` always can catch up ```slow```
  - 10 + 1 - 2 + 1 - 2 + 1 - 2 ... = 0
