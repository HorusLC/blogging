from services.idgenerator import IdGenerator


class Repository:
    def __init__(self, id_generator: IdGenerator):
        self._entities: dict = {}
        self._idGenrator = id_generator

    def __len__(self):
        return self.count()

    def __add__(self, other):
        self._entities.update(other._entities)
        return self

    def __iter__(self):
        # return iter(self._entities.values())
        # return RepositoryIterator(self._entities.values())
        for entity in self._entities.values():
            yield entity

    def find_all(self):
        return self._entities.values()

    def find_by_id(self, id_):
        found = self._entities.get(id_)
        if found is None:
            raise Exception(f'Entity with ID:{id_} not found')
        return found

    def create(self, entity):
        entity.id_ = self._idGenrator.get_next_id()
        self._entities[entity.id_] = entity
        return entity

    def update(self, entity):
        self.find_by_id(entity.id_)
        self._entities[entity.id_] = entity
        return entity

    def delete_by_id(self, id_):
        old = self.find_by_id(id_)
        del self._entities[id_]
        return old

    def count(self):
        return len(self._entities)
