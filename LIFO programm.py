import queue


class MyLifo:
    def __init__(self):
        self.fifo = queue.Queue()

    def isEmpty(self):
        return self.fifo.empty()

    def push(self, x):
        self.fifo.put(x)

    def pop(self):
        for _ in range(len(self.fifo.queue) - 1):
            self.push(self.fifo.get())
        return self.fifo.get()

lifo = MyLifo()
i = 0

while (i < 30):
    lifo.push(i)
    i += 1

while (lifo.isEmpty() == False):
    print(lifo.pop(), end=" ")
    