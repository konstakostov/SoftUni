from abc import ABC, abstractmethod
import time


class Work(ABC):
    @abstractmethod
    def work(self):
        ...


class Eat(ABC):
    @abstractmethod
    def eat(self):
        ...


class Worker(Work, Eat):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Work):
    def work(self):
        print("I'm a robot. I'm working....")


class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...

        self.worker = worker


class WorkManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, Work):
            print(f"`worker` must be of type {self.__class__.__name__}")

        self.worker = worker

    def manage(self):
        self.worker.work()


class EatManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, Eat):
            print(f"`worker` must be of type {self.__class__.__name__}")

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = EatManager()

work_manager.set_worker(Worker())
break_manager.set_worker(Worker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()


break_manager.set_worker(Robot())
break_manager.lunch_break()
