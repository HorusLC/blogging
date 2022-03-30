import abc
from abc import ABC


class IdGenerator(ABC):
    @abc.abstractmethod
    def get_next_id(self):
        pass
    