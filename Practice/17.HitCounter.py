from collections import deque

class HitCounter:
    def __init__(self):
        # Hint: Store items as [timestamp, count]
        self.hits = deque()
        self.total_hits = 0
        self.timestamp = []
        self.count = 0

    def hit(self, timestamp: int) -> None:
        # 1. If the deque isn't empty and the last timestamp is the same, 
        #    just increment the count of the last element.
        if len(self.hits) > 0 and self.timestamp == timestamp:
            self.count += 1
        # 2. Otherwise, append [timestamp, 1].
        else:
            self.timestamp.append(1)
        # 3. Always increment self.total_hits.
        self.total_hits += 1
        pass

    def getHits(self, timestamp: int) -> int:
        # 1. While hits exist and the oldest hit (hits[0][0]) 
        #    is <= timestamp - 300:
        # 2.   Pop the oldest hit and subtract its count from total_hits.
        # 3. Return total_hits.
        pass

# Test code:
# counter = HitCounter()
# counter.hit(1)
# counter.hit(2)
# counter.hit(3)
# print(counter.getHits(4))  # Expected: 3
# counter.hit(300)
# print(counter.getHits(300)) # Expected: 4
# print(counter.getHits(301)) # Expected: 3 (The hit at timestamp 1 is gone)