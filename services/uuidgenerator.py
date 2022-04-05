from services.idgenerator import IdGenerator
import uuid


class UuidGenerator(IdGenerator):

    def get_next_id(self):
        return str(uuid.uuid1())

