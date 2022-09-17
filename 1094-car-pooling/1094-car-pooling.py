class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        in_car, passengers = 0, {i:0 for i in range(1001)}
        for [num, f, t] in trips:
            passengers[f] += num
            passengers[t] -= num
        for i in range(1001):
            in_car += passengers[i]
            if in_car > capacity: return False
        return True