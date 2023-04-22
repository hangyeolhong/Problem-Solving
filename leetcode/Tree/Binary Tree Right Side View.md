### Python solution
```python
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        q = deque()

        if root:
            q.append(root)

        while q:
            rightMost = None
            for _ in range(len(q)):
                cur = q.popleft()
                rightMost = cur

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if rightMost == None:
                break

            answer.append(rightMost.val)
        return answer
```

### Explanation
- Keep ```rightMost``` node to find the last inserted node
- ```[1, null, 3]``` returns ```[1, 3]```
- ```[1, 2]``` returns ```[1, 2]```
