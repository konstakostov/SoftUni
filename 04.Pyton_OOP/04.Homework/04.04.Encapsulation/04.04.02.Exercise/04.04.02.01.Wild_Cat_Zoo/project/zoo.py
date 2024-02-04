from typing import List

from project import Animal
from project import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: str, price: int) -> str:
        is_capacity = self.__animal_capacity > len(self.animals)
        is_budget = self.__budget >= price

        if is_capacity and is_budget:
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_capacity and not is_budget:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        needed_money = sum([w.salary for w in self.workers])

        if self.__budget < needed_money:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        needed_money = sum([a.money_for_care for a in self.animals])

        if self.__budget < needed_money:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"

        result += f"----- {len(lions)} Lions:\n"
        for l in lions:
            result += f"{l.__repr__()}\n"

        result += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            result += f"{t.__repr__()}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            result += f"{c.__repr__()}\n"

        return result.strip()

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"

        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            result += f"{k.__repr__()}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            result += f"{c.__repr__()}\n"

        result += f"----- {len(vets)} Vets:\n"
        for v in vets:
            result += f"{v.__repr__()}\n"

        return result.strip()
