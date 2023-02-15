class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        answer = [0 for _ in range(len(temperatures))]

        for idx, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                day = st.pop()
                answer[day] = idx - day

            st.append(idx)

        return answer
