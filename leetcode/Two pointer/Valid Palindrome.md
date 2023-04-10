### Python solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        res = ""
        for c in s:
            if c.isalnum():
                res += c

        left, right = 0, len(res) - 1

        while left <= right:
            if res[left] != res[right]:
                return False

            left += 1
            right -= 1

        return True
```
