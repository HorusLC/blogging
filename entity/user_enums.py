from enum import Enum


class Role(Enum):
    BLOGGER = 1
    ADMIN = 2

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return {
            'name': self.name,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class Gender(Enum):
    Male = 1
    Female = 2

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return {
            'name': self.name,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }