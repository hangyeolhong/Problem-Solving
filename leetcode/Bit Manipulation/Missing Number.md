### Python solution
```python
#1. XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = len(nums)

        for i in range(len(nums)):
            answer ^= (i ^ nums[i])

        return answer
        
#2. Sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = sum([i for i in range(len(nums) + 1)])

        for i in range(len(nums)):
            answer -= nums[i]

        return answer
```

### Explanation
- Key: Order doesn't matter
- XOR between same number results in **0**.
