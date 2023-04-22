### Python solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy is used to keep the head of the new list
        # cur is used for saving the current last element when creating the list during the while statement

        dummy = ListNode()
        cur = dummy
        print("id check", id(cur), id(dummy))   # same id (mutable)

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1        # dummy also changes
                list1 = list1.next

            else:
                cur.next = list2        # dummy also changes
                list2 = list2.next
            cur = cur.next              # reassign cur -> cur points to new object 

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
```

### Drawing Explanation
<img src="https://user-images.githubusercontent.com/59331040/233763891-fe0fea1c-3e8f-40da-b254-ed61df2522dd.JPG" width="50%">
