### Python solution
```python
import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
        if len(self.large) + 1 < len(self.small):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

### Explanation
- Use 2 heap: min, max heap
  - Size of min, max heap is approximately same.
- Pop an element in the heap is O(1)

### Follow-up
- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
  - Use Counter dictionary and iterate over the array to find the middle value to get our median ( O(100))
- If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
  - Just keep a count of how many numbers are above 100 and how many numbers are below 0, since these numbers could never get to be the median and are therefore not important to keep  (O(100))
- 


