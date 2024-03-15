animals = input().split(", ")

animals_list = list(animals)

search = "wolf"

index = animals_list.index(search)

if index + 1 == len(animals_list):
    print(f"Please go away and stop eating my sheep")
else:
    animals_list.reverse()
    index = animals_list.index(search)
    print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
