import json
from utils import jsonmapping as mapping

from dao.repository_base import Repository


class JsonRepository(Repository):

    def __init__(self, id_generator, db_filename):
        super().__init__(id_generator)
        self.db_filename = db_filename

    def save(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            json.dump(list(self.find_all()), f, indent=4, default=mapping.dumper)

    def load(self):
        self.clear()
        with open(self.db_filename, "rt", encoding="utf-8") as f:
            entities = json.load(f, object_hook=mapping.object_hook)
            self.add_all(entities)







