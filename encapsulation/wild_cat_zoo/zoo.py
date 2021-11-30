from encapsulation.wild_cat_zoo.animal import Animal
from encapsulation.wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name, budget: int, animal_capacity: int, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} " \
               f"added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} " \
               f"hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy." \
                   f" Budget left: {self.__budget}"
        return "You have no budget to pay your workers." \
               " They are unhappy"

    def tend_animals(self):
        care_total = sum([x.money_for_care for x in self.animals])
        if self.__budget < care_total:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= care_total
        return f"You tended all the animals. They are happy. " \
               f"Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        info = f"You have {len(self.animals)} animals\n"
        info += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            info += f"{lion.__repr__()}\n"
        info += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            info += f"{tiger.__repr__()}\n"
        info += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            info += f"{cheetah.__repr__()}\n"
        return info.strip()

    def workers_status(self):
        info = f"You have {len(self.workers)} workers\n"

        info += self.__get_workers_status_by_type("Keeper")
        info += self.__get_workers_status_by_type("Caretaker")
        info += self.__get_workers_status_by_type("Vet")

        return info.strip()

    def __get_workers_status_by_type(self, worker_type):
        workers = [str(x) for x in self.workers if x.__class__.__name__ == worker_type]

        info = f"----- {len(workers)} {worker_type}s:\n"
        for worker in workers:
            info += worker
            info += "\n"

        return info
