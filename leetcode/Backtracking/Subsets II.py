class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        res = []
        nums.sort()

        def dfs(idx):
            if idx >= len(nums):
                answer.append(res[::])
                return

            res.append(nums[idx])
            dfs(idx + 1)
            res.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)

        dfs(0)
        return answer
