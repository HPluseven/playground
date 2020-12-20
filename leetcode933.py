class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        if len(self.queue) > 3001:
            self.queue.pop(0)
        start = 0
        for idx, item in enumerate(self.queue):
            if item >= t-3000:
                start = idx
                break

        return len(self.queue[start:])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
