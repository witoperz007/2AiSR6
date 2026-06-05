class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1
        return self.counter
    def decrement(self):
        self.counter -= 1
        return self.counter
