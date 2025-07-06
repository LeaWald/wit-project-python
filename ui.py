from abc import ABC, abstractmethod

class ui(ABC):

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def add(self, path_file):
        pass

    @abstractmethod
    def commit(self, message):
        pass

    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def checkout(self, commit_id):
        pass