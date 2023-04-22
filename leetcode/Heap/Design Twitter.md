### Python solution
```python
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.f = defaultdict(set)
        self.q = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.q, (-1 * self.time, tweetId, userId))   # max heap, pop the most recent tweet
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        answer = []
        tmp = []

        while self.q and len(answer) < 10:
            time, t, u = heapq.heappop(self.q)
            heapq.heappush(tmp, (time, t, u))

            if u == userId or u in self.f[userId]:
                answer.append(t)

        while tmp:
            time, t, u = heapq.heappop(tmp)
            heapq.heappush(self.q, (time, t, u))

        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.f:
            # Prevent Key error
            self.f[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

### Explanation
- Data structure
- To prevent key error, use
  - ```if followerId in self.f:```
