### Python solution
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left, right = 1, piles[-1]
        answer = 1

        while left <= right:
            mid = (left + right) // 2

            time = 0
            for pile in piles:
                if pile % mid == 0:
                    time += (pile // mid)
                else:
                    time += (pile // mid) + 1

            if time <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
```

### Drawing explanation
<img src="https://user-images.githubusercontent.com/59331040/219842051-009789d2-c35b-4c8e-b0de-0e9b6b3c836d.png" width="70%"/>
