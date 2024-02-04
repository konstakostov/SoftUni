from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self) -> None:
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def __find_player_by_name(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                return player

    @staticmethod
    def __check_if_players_cant_win(*players):
        result = []

        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

    @staticmethod
    def __attack_round(p1, p2):
        p2.stamina -= (p1.stamina / 2)

        if p1.stamina - (p1.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)

        if p1.stamina < p2.stamina:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    def add_player(self, *players: Player):
        new_players = []

        for player in players:
            if player not in self.players:
                self.players.append(player)

                new_players.append(player.name)

        return f"Successfully added: {', '.join(new_players)}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ["Food", "Drink"]:
            return

        player = self.__find_player_by_name(player_name)
        supply = next(filter(lambda f: type(f).__name__ == sustenance_type, self.supplies), None)

        if player.stamina >= Player.MAX_STAMINA:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food" and not supply:
            raise Exception("There are no food supplies left!")

        if sustenance_type == "Drink" and not supply:
            raise Exception("There are no drink supplies left!")

        if player.stamina + supply.energy >= 100:
            player.stamina = Player.MAX_STAMINA
        else:
            player.stamina += supply.energy

        self.supplies.remove(supply)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        is_no_duel = self.__check_if_players_cant_win(first_player, second_player)
        if is_no_duel:
            return is_no_duel

        if first_player.stamina < second_player.stamina:
            return self.__attack_round(first_player, second_player)
        else:
            return self.__attack_round(second_player, first_player)

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info)
        return result
