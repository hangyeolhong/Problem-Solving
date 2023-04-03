### Python solution
```python
#1. Two-pointer
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        answer = 0

        left, right = 0, len(people) - 1

        while left < right:
            if people[left] + people[right] == limit:
                answer += 1
                left += 1
                right -= 1
            
            elif people[left] + people[right] < limit:
                answer += 1
                left += 1
                right -= 1

            else:
                answer += 1
                right -= 1

        if left == right: answer += 1

        return answer


#2. Opitimized version of #1
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        answer = 0

        left, right = 0, len(people) - 1

        while left < right:
            answer += 1

            if people[left] + people[right] <= limit:
                left += 1
            right -= 1

        if left == right: answer += 1

        return answer
        
        
#3. Bucket sort
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        bucket = [0] * (limit + 1)
        for p in people:
            bucket[p] += 1

        answer = 0
        start, end = 0, limit

        while start <= end:
            # valid position
            while start <= end and bucket[start] <= 0: start += 1
            while start <= end and bucket[end] <= 0: end -= 1

            if bucket[start] <= 0 and bucket[end] <= 0: break

            answer += 1
            if start + end <= limit: bucket[start] -= 1
            bucket[end] -= 1

        return answer
```

### Explanation
- Each boat carries **at most two people** at the same time.
