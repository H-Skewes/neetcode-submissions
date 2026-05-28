class MyHashMap:

    def __init__(self):
        self.current_hash = [None] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.current_hash[key] = value

    def get(self, key: int) -> int:
        value = self.current_hash[key]
        return value if value is not None else -1
  

    def remove(self, key: int) -> None:
        self.current_hash[key] = None      


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)