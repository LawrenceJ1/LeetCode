class UndergroundSystem:

    def __init__(self):
        self.dict = defaultdict(list)
        self.pairs = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.pairs[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, startTime = self.pairs[id]
        self.dict[(start, stationName)].append(t-startTime)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.dict[(startStation, endStation)])/len(self.dict[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)