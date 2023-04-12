### Python solution
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            next_dp = set()

            for t in dp:
                if t + nums[i] == target:
                    return True

                next_dp.add(t + nums[i])
                next_dp.add(t)

            dp = next_dp

        return False
```
