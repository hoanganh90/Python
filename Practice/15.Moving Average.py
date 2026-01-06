from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.current_sum = 0 # Pro-tip: Keep track of sum to avoid re-calculating!

    def next(self, val: int) -> float:
        # 1. Add the new value to the queue and the current_sum
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.current_sum += val
        # 2. If the queue is larger than self.size, remove the oldest item
        #    (Hint: use self.queue.popleft() and subtract that value from current_sum)
        elif len(self.queue) == self.size:
            temp = self.queue.popleft()
            self.queue.append(val)
            self.current_sum -= temp
            self.current_sum += val
        # 3. Return the average (current_sum divided by length of queue)
        return self.current_sum / len(self.queue)
        pass

# Test code:
m = MovingAverage(3)
print(m.next(1))  # Expected 1.0
print(m.next(10)) # Expected 5.5
print(m.next(3))  # Expected 4.66...
print(m.next(5))  # Expected 6.0