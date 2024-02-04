from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(BaseWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")


class UltraWorker(BaseWorker):
    @staticmethod
    def work():
        print("I work 24/7")


class LazyWorker(BaseWorker):
    @staticmethod
    def work():
        print("I worked for 5 minutes total last month!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f"`worker` must be of type {BaseWorker}")

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
super_worker = SuperWorker()
ultra_worker = UltraWorker()
lazy_worker = LazyWorker()


manager.set_worker(worker)
manager.manage()

manager.set_worker(super_worker)
manager.manage()

manager.set_worker(ultra_worker)
manager.manage()

manager.set_worker(lazy_worker)
manager.manage()
