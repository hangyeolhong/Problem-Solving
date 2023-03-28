### Python solution
```python
# shortest sequence -> shortest path algorithm
# maximum wordList length = 5000 -> TLE caution

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # base case
        if endWord not in wordList:
            return 0

        # make pattern dict
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]     # slicing ---> index error X
                d[pattern].append(word)
        
        q = deque()
        visit = set()
        visit.add(beginWord)
        q.append(beginWord)
        res = 1

        while q:
            # snapshot current q
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    if pattern in d:
                        for next_word in d[pattern]:
                            if next_word not in visit:
                                visit.add(next_word)
                                q.append(next_word)

            res += 1

        return 0
```

### Similar idea
[Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
