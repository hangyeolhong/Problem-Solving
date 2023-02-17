class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.candidates = candidates
        self.candidates.sort()

        self.dfs([], 0, target)
        return self.answer


    def dfs(self, res, idx, target):
        if sum(res) == target:
            self.answer.append(res)
            return
        
        if idx == len(self.candidates):
            return

        for i in range(idx, len(self.candidates)):
            if i > idx:
                if self.candidates[i - 1] == self.candidates[i]:
                    # 중복 방지
                    continue

            if sum(res) + self.candidates[i] <= target:
                self.dfs(res + [self.candidates[i]], i + 1, target)


"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res
"""
