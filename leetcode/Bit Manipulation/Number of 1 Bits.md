### Python solution
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            n &= (n - 1)
            res += 1
        
        return res
```

### Explanation
- ```n - 1``` means decrease 1 of the lower digit.
  - ex) 1011 becomes 1010.
- ```n &=``` means update n.
  - Because of AND op, 1 of the higher side of n is maintained, and the part where 1 is missing changes.
  - ex) 1011 & 1010 = 1010
