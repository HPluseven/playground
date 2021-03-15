class MyHashSet:

    def __init__(self):
        self.base = 769
        self.data = [[] for _ in range(self.base)]

    def add(self, key: int) -> None:
        h = self.hash(key)
        for ele in self.data[h]:
            if ele == key:
                return

        self.data[h].append(key)

    def remove(self, key: int) -> None:
        h = self.hash(key)
        for ele in self.data[h]:
            if ele == key:
                self.data[h].remove(key)
                return

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        for ele in self.data[h]:
            if ele == key:
                return True
        return False

    def hash(self, key):
        return key % self.base


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
