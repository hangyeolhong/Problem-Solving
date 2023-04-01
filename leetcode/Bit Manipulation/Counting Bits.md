### Python solution
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == 2 * offset:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp
```

### Explanation
- 0: 0000

==========
\# offset = 1
- 1: 0001       

==========
\# offset = 2
- 2: 0010    
- 3: 0011

==========
\# offset = 4
- 4: 0100     
- 5: 0101
- 6: 0110
- 7: 0111

==========
\# offset = 8
- 8: 1000     
