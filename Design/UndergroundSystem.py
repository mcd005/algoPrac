
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# Dict of active journeys that looks like { id: (stationStart, timeStart)}
# Checking in adds an active joruney to this dict
# Checking out means we remove journey from map
# But then we also add to our dict of routes which looks like { startDest1: {endDest1: [total time, total trips]}}
# Get average will be just time, trips = routes[startDest][endDest]; return time/trips
from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.active_journeys = {}
        self.routes = defaultdict(lambda: defaultdict(lambda: [0, 0]))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active_journeys[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.active_journeys.pop(id)
        self.routes[start_station][stationName][0] += (t - start_time)
        self.routes[start_station][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.routes[startStation][endStation]
        return total_time / total_trips