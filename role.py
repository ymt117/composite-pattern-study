from abc import ABCMeta, abstractmethod

class Role(metaclass=ABCMeta):
    @abstractmethod
    def get_members(self):
        pass