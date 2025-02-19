class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = []
        self.limit = limit
        for item in items:
            if not self.full():
                self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        return -1