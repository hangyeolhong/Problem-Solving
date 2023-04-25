### Python solution
```python
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        d = {}
        for n in hand:
            d[n] = 1 + d.get(n, 0)

        lst = list(d.keys())
        heapq.heapify(lst)

        while lst:
            first = lst[0]
            
            for n in range(first, first + groupSize):
                if n not in d:
                    return False
                if d[n] == 0:
                    return False

                d[n] -= 1

                if d[n] == 0:
                    # n cannot be used again
                    heapq.heappop(lst)
                
        return True
```
