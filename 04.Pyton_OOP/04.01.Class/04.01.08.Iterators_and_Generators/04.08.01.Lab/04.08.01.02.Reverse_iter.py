class reverse_iter:
    def __init__(self, collection):
        self.collection = collection

        self.start = len(self.collection) - 1
        self.stop = 0

        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            raise StopIteration()

        tmp = self.current
        self.current -= 1

        return self.collection[tmp]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
