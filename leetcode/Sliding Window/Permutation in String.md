### Python solution
```python
"""
# TLE
from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = list(map(''.join, permutations(s1)))

        for i in range(len(s)):
            if s[i] in s2:
                return True

        return False
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d1, d2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            d1[ord(s1[i]) - ord('a')] += 1
            d2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += (1 if d1[i] == d2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            
            d2[idx] += 1
            if d1[idx] == d2[idx]:
                matches += 1
            elif d1[idx] + 1 == d2[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            d2[idx] -= 1
            if d1[idx] == d2[idx]:
                matches += 1
            elif d1[idx] - 1 == d2[idx]:
                matches -= 1
            l += 1

        return matches == 26
```
