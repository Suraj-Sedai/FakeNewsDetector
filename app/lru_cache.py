class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        else:
            self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.cache:
            print("GET MISS: key = {key}")
            return None
        else:
            print("GET HIT: key = {key}")
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_front(node)
            return node.value
        
    def put(self, key, value):
        #If key exists → update value + move to front
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_front(node)
            print("UPDATE: Key={key} value = {value}")
        else:
            new_node = Node(key, value)
            self._add_to_front(new_node)
            print("PUT: Key={key} value = {value}")
            
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.cache[node.key] = node
        
        if len(self.cache) > self.capacity:
            # Remove the least recently used item
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.cache[lru_node.key]

    
    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def __str__(self):
        result = []
        current = self.head.next

        while current != self.tail:
            result.append((current.key, current.value))
            current = current.next

        return str(result)