class MyHashSet:

    def __init__(self):
        self.current_hash = []

    def add(self, key: int) -> None:
        if key not in self.current_hash:
            self.current_hash.append(key)

    def remove(self, key: int) -> None:
        if key in self.current_hash:
            self.current_hash.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.current_hash


