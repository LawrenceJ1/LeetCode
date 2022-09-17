class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        days = deque()
        for i, x in enumerate(temperatures):
            while days and x > temperatures[days[-1]]:
                answer[days[-1]] = i-days[-1]
                days.pop()
            days.append(i)
        return answer