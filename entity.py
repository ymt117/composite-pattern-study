from abc import ABCMeta, abstractmethod

class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass