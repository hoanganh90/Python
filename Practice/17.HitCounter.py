from collections import deque

class HitCounter:
    def __init__(self):
        # Hint: Store items as [timestamp, count]
        #Imagine our self.hits deque looks like this: deque([ [10, 5], [15, 2], [20, 8] ])

        # The first [0] accesses the first element in the deque.

        # self.hits[0] returns the first "package": [10, 5].

        # The second [0] accesses the first value inside that package.

        # self.hits[0][0] returns the timestamp: 10. TIME

        # self.hits[0][1] would return the count: 5. COUNT
        self.hits = deque()
        self.total_hits = 0

    def hit(self, timestamp: int) -> None:
        # 1. If the deque isn't empty and the last timestamp is the same, 
        #    just increment the count of the last element.
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        # 2. Otherwise, append [timestamp, 1].
        else:
            self.hits.append([timestamp, 1])
        # 3. Always increment self.total_hits.
        self.total_hits += 1
        pass

    def getHits(self, timestamp: int) -> int:
        # 1. While hits exist and the oldest hit (hits[0][0]) 
        #    is <= timestamp - 300:
        while self.hits and self.hits[0][0] <= timestamp - 300:
        # 2.   Pop the oldest hit and subtract its count from total_hits.
        # 3. Return total_hits.
            old_timestamp, count = self.hits.popleft()
            self.total_hits -= count
        return self.total_hits

# Test code:
counter = HitCounter()
counter.hit(1)
counter.hit(2)
counter.hit(3)
print(counter.getHits(4))  # Expected: 3
counter.hit(300)
print(counter.getHits(300)) # Expected: 4
print(counter.getHits(301)) # Expected: 3 (The hit at timestamp 1 is gone)
