from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.passenger_in = {}
        self.duration = defaultdict(int)
        self.count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        lastStationName, start_t = self.passenger_in.pop(id)
        self.duration[(lastStationName, stationName)] += t - start_t
        self.count[(lastStationName, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.duration[(startStation, endStation)] / self.count[(startStation, endStation)]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
