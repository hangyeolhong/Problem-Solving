from collections import defaultdict

# Count the occurrences of each character in both string

"""
#1. sorting
# Time complexity: O(nlogn)
# Space complexity: O(1)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
"""

#2. Hashmap
# Time complexity: O(len(s) + len(t))
# Space complexity: O(len(s) + len(t))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
          
        d = defaultdict(int)

        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1

        for k, v in d.items():
            if v != 0:
                return False
        return True
