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

