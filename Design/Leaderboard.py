# Version 1 - Dict and heap
class Leaderboard:
    # TC    O(1)
    # SC    O(1)
    def __init__(self):
        self.m = defaultdict(int)

    # TC    O(1)
    # SC    O(n)
    def addScore(self, playerId: int, score: int) -> None:
        self.m[playerId] += score

    # TC    O(nlogk) - we heapify first k then pushpop the other n - k elements to that small heap
    # SC    O(k)
    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.m.values()))

    # TC    O(1)
    # SC    O(1)
    def reset(self, playerId: int) -> None:
        del self.m[playerId]


# Version 2 - OrderedDict most_common
class Leaderboard(object):

    def __init__(self):
        self.A = collections.Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    # TC    O(nlogk) - we heapify first k then pushpop the other n - k elements to that small heap
    # SC    O(k)
    def top(self, K):
        return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0