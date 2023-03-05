### Python solution
```python
#1. dp O(n^2) (3sec)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

      
#2. binary search (84ms)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        answer = []

        # return the first index where nums[ret] less than n is located (* strictly increasing)
        def getIdx(lst, n):
            left, right = 0, len(lst) - 1
            ret = -1

            while left <= right:
                mid = (left + right) // 2
                if lst[mid] < n:
                    ret = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ret


        for i in range(len(nums)):
            idx = getIdx(answer, nums[i])
            if idx == len(answer) - 1:
                # end of list
                answer.append(nums[i])
            else:
                answer[idx + 1] = nums[i]
        
        return len(answer)
```
