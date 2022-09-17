class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = deque()
        min_dif = arr[1]-arr[0]
        for i in range(1, len(arr)):
            x = arr[i]-arr[i-1]
            if x < min_dif:
                min_dif = x
                ans = deque()
                ans.append([arr[i-1],arr[i]])
            elif x == min_dif:
                ans.append([arr[i-1],arr[i]])
        return ans