from enum import Enum


class BlogCategory(Enum):
    IT = 1
    Lifestyle = 2
    Nature = 3
    Cooking = 4
    Poetry = 5
    Literature = 6
    Sports = 7

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return {
            'name': self.name,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }