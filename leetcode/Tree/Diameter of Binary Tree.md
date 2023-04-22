### Python solution
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(r):
            nonlocal res
            
            # End condition
            if not r:
                return 0

            left = dfs(r.left)
            right = dfs(r.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
```

### Explanation
- global vs nonlocal
