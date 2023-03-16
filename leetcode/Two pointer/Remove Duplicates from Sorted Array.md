### Python solution
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1
```

### Explanation
```
pointer i -> points unique elements
pointer j -> points new elements

if nums[i] != nums[j], nums[j] is new unique element, therefore add nums[j] to next i.
```
