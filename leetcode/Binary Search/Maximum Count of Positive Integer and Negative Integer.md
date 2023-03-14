### Python solution
```python
from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # binary search: find the first and last insert position of 0

        def find_first(nums, left, right):
            first = 0

            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == 0 and (mid == 0 or nums[mid - 1] < 0):
                    return mid
                
                if nums[mid] < 0:
                    first = mid + 1  # insert at next position (mid + 1)
                    left = mid + 1
                else:
                    right = mid - 1

            return first


        def find_last(nums, left, right):
            last = 0

            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == 0 and (mid == len(nums) - 1 or nums[mid + 1] > 0):
                    return mid
                
                if nums[mid] <= 0:
                    left = mid + 1
                else:
                    last = mid - 1  
                    right = mid - 1

            return last

          
        left, right = 0, len(nums) - 1
        neg = find_first(nums, left, right)
        pos = len(nums) - find_last(nums, left, right) - 1
        
        return max(pos, neg)
```
