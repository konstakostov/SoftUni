class reverse_iter:
    def __init__(self, iters):
        self.iters = iters

        self.start = len(self.iters) - 1
        self.end = 0

        self.index = len(self.iters)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1

        if self.index < self.end:
            raise StopIteration

        return self.iters[self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
