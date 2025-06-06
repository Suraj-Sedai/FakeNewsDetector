from collections import deque

class ArticleQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, article):
        self.queue.append(article)
    
    def dequeue(self):
        return self.queue.popleft() if self.queue else None
    
    def is_empty(self):
        return len(self.queue) == 0
    
class SeenURLs:
    def __init__(self):
        self.seen = set()
    
    def has_seen(self, url):
        return url in self.seen

    def add_url(self,url):
        self.seen.add(url)


class HistoryStack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) ==0
    
    def clear(self):
        self.stack.clear()