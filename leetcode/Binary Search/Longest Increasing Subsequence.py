class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # find first index to put n in lst
        def getIdx(lst, n):
            left, right = 0, len(lst) - 1
            ret = -1

            while left <= right:
                mid = (left + right) // 2
                if lst[mid] < n:
                    ret = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return ret


        answer = []

        for i in range(len(nums)):
            idx = getIdx(answer, nums[i])
            
            if idx == len(answer) - 1:
                answer.append(nums[i])
            else:
                answer[idx + 1] = nums[i]
        
        return len(answer)
