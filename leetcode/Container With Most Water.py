class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        answer = 0
        
        while i < j:
            if height[i] <= height[j]:
                # i 기준 면적 계산
                answer = max(answer, height[i] * (j - i))
                i += 1
            else:
                # j 기준 면적 계산
                answer = max(answer, height[j] * (j - i))
                j -= 1   
                        
        return answer
