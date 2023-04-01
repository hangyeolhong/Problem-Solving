### Python solution
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0     # n ^ 0 = n
        for num in nums:
            res ^= num

        return res
```

### Explanation
- Every element appears twice except for one
  - In XOR, order doesn't matter.
  - Therefore, XOR between same value (element that appears twice) results in 0.
  - Finally, XOR between 0 and element that appears once results in **single number**.
