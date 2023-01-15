class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]

        for i in range(1, len(nums)):
            pref.append(pref[-1] * nums[i - 1])

        # reverse
        suffix = [1]
        for i in range(len(nums) - 2, -1, -1):
            suffix.append(suffix[-1] * nums[i + 1])

        suffix.reverse()

        return [pref[i] * suffix[i] for i in range(len(nums))]
