from typing import List

from project import Animal
from project import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: str, price: int) -> str:
        is_capacity_left = self.__animal_capacity > len(self.animals)
        is_budget = self.__budget >= price

        if is_capacity_left and is_budget:
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_capacity_left and not is_budget:
            return f"Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker) -> str:
        if not self.__workers_capacity > len(self.workers):
            return f"Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            self.__budget -= worker.salary  # WHY!?!?!??!?!?!??!?!?!?!?

            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        needed_amount = sum([w.salary for w in self.workers])

        if self.__budget >= needed_amount:
            self.__budget -= needed_amount

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        needed_amount = sum([w.money_for_care for w in self.animals])

        if self.__budget >= needed_amount:
            self.__budget -= needed_amount

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"
        for l in lions:
            result += f"{l}\n"

        result += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            result += f"{t}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            result += f"{c}\n"

        return result[:-1]

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        caretakers = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        vets = [a for a in self.workers if a.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            result += f"{k}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            result += f"{c}\n"

        result += f"----- {len(vets)} Vets:\n"
        for v in vets:
            result += f"{v}\n"

        return result [:-1]


