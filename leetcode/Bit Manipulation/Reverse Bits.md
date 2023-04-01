### Python solution
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1     # n & 1 = n
            res |= (bit << (31 - i))

        return res
```

### Explanation
- Simple: bit shifting 
  - ```n & 1 = n```
  - ```bit = (n >> i) & 1``` only considers the last bit of n.
  - ```res |= (bit << (31 - i))``` adds bit from high to low.
