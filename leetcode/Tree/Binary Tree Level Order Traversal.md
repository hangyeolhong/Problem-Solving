### Python solution
```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        q = deque()

        if root:
            q.append(root)

        while q:
            tmp = []
            # for level-order (BFS)
            for _ in range(len(q)):
                cur = q.popleft()
                tmp.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            answer.append(tmp)

        return answer
```
