from typing import List

from project import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name

        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        pokemons_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])
        result += pokemons_data

        return result.strip()
