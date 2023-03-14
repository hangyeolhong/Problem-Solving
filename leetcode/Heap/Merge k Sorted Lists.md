### Python solution
```python
# Sol1 - connecting all the k linked lists into one list, and sort the list.
# this is simple but it does not take the advantage of the fact that each linked list is already sorted.

# Sol1 - use min heap data structure.
# -> give us the min element at each step


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode()
        p = res

        for i, h in enumerate(lists):
            if h:
                heappush(heap, (h.val, i))

        while heap:
            val, i = heappop(heap)
            n = lists[i]
            p.next = n
            p = n
            if n.next:
                heappush(heap, (n.next.val, i))
                lists[i] = n.next
        return res.next
```
