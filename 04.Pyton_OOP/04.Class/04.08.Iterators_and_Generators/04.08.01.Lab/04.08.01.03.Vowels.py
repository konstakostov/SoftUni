class vowels:
    def __init__(self, text: str):
        self.text = text

        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']

        self.current = -1
        self.end = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1

        if self.current > self.end:
            raise StopIteration

        current_elem = self.text[self.current]

        if current_elem.lower() in self.vowels:
            return current_elem

        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
