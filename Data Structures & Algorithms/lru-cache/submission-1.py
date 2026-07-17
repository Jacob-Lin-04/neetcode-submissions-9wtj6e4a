from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Use OrderedDict to remember order keys are inserted
        self.cache = OrderedDict()  
        self.cap = capacity

    def get(self, key: int) -> int:
        # If key is not in cache return -1
        if key not in self.cache:
            return -1
        
        # Move key recently accessed to the end
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Move key just inserted 
        if key in self.cache:
            self.cache.move_to_end(key)

        # Store key value pair
        self.cache[key] = value

        # If length exceeds capacity pop the oldest item
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
        
