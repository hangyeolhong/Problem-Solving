class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # search right side (right has the min)
                left = mid + 1
            else:
                # search left side (left has the min)
                right = mid

        return nums[left]
