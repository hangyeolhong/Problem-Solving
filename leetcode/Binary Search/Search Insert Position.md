### Python solution
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search: sorted array

        left, right = 0, len(nums) - 1

        answer = -1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                answer = mid
                break
            
            elif nums[mid] < target:
                answer = mid + 1  # insert at next position (mid + 1)
                left = mid + 1
            else:
                right = mid - 1
        
        return answer
```
