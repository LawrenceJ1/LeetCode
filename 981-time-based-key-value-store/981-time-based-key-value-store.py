class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        return(self.binary_search(0, len(self.dict[key]), self.dict[key], timestamp))

    def binary_search(self, left, right, ans, time):
        if left >= right:
            if left < len(ans) and ans[left][1] <= time:
                return ans[left][0]
            return ""
        if ans[(left+right)//2][1] == time:
               return ans[(left+right)//2][0]
        elif ans[(left+right)//2][1] > time:
               return self.binary_search(left, ((left+right)//2)-1, ans, time)
        elif ans[(left+right)//2][1] < time:
               return self.binary_search(((left+right)//2)+1, right, ans, time) or ans[(left+right)//2][0]
               
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)