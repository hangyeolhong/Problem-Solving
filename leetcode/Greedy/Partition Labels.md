### Python solution
```python3
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        cnt = {}
        answer = []

        for i in range(len(S)):
            cnt[S[i]] = i
        
        j = 0
        goal = 0
        l = 0

        while j < len(S):
            cur = cnt[S[j]]
            goal = max(cur, goal)
            l += 1

            if goal == j:
                answer.append(l)
                l = 0

            j += 1

        return answer
```
