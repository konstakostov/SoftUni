class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

        self.index = self.count + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.end:
            raise StopIteration

        self.index -= 1

        return self.index


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print()

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
