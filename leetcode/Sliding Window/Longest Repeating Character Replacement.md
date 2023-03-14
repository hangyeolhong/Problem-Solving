### Python solution
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = dict()

        l = 0
        maxf = -1
        res = 0

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxf = max(maxf, cnt[s[r]])

            if (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
```
