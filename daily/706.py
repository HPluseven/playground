class MyHashMap:

    def __init__(self):
        self.base = 769
        self.data = [[] for _ in range(self.base)]

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        it = self.data[h]
        for ele in it:
            if ele[0] == key:
                ele[1] = value
                return

        it.append([key, value])

    def get(self, key: int) -> int:
        h = self.hash(key)
        it = self.data[h]

        for ele in it:
            if ele[0] == key:
                return ele[1]

        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        it = self.data[h]

        for ele in it:
            if ele[0] == key:
                it.remove(ele)
                return

    def hash(self, key):
        return key % self.base


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
