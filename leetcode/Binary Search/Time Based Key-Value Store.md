### Python solution
```python

class TimeMap:

    def __init__(self):
        self.timemap = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap.get(key, [])
        l, r = 0, len(values) - 1
        answer = -1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                answer = mid
                l = mid + 1
            else:
                r = mid - 1

        if answer == -1:
            return ""
        else:
            return values[answer][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

### Explanation
1. All the timestamps timestamp of set are strictly increasing. ---> we don't need to sort self.timemap[key]
2. Prevent the key error of dictionary ---> values = self.timemap.get(key, [])
