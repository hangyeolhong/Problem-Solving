### Python solution
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(cur, left, right):
            if not cur:
                return True

            if not (left < cur.val < right):
                return False

            return dfs(cur.left, left, cur.val) and dfs(cur.right, cur.val, right)

        return dfs(root, float('-inf'), float('inf'))
```

### Explanation
- BST
  - At first, define left and right boundary to ```-inf```and ```inf``` respectively.
  - When move to left child tree, update right boundary to current node's value.
  - When move to right child tree, update left boundary to current node's value.
