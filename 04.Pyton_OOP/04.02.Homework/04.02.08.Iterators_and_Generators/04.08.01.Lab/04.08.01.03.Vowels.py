class vowels:
    def __init__(self, text):
        self.text = text

        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']

        self.end = len(text) - 1
        self.index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index > self.end:
            raise StopIteration

        current = self.text[self.index]

        if current.lower() in self.vowels:
            return current

        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
