class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "04.10.02.01.Mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "04.10.02.01.Mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)} " \
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)} " \
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)} " \
                   f"\nTotal animals: {Zoo.__animals}"


zoo_name = input()
animals_count = int(input())

zoo = Zoo(zoo_name)

for _ in range(animals_count):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()

print(zoo.get_info(info))
