from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = defaultdict(list)

        for s in strs:
            lst[''.join(sorted(s))].append(s)

        return list(lst.values())
