class FreqStack:
    def __init__(self):
        self.freq = defaultdict(list)
        self.count = Counter()
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        freq = self.count[val]+1
        self.count[val] = freq
        if freq > self.max_freq:
            self.max_freq = freq
        self.freq[freq].append(val)
        
    def pop(self) -> int:
        ans = self.freq[self.max_freq].pop()
        self.count[ans] -= 1
        if not self.freq[self.max_freq]:
            self.max_freq -= 1
        return ans
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()