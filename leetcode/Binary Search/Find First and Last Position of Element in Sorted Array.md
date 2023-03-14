### Python solution
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] < target:
                        return mid

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        
        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        return mid

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        return [find_first(nums, target), find_last(nums, target)]
```
