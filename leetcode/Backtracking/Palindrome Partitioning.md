### Python solution
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrom(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res, part = [], []
        
        def dfs(idx):
            if idx >= len(s):
                res.append(part[:])
                return

            for j in range(idx, len(s)):
                if is_palindrom(idx, j):
                    part.append(s[idx:j + 1])
                    dfs(j + 1)
                    part.pop()


        dfs(0)
        return res
```
