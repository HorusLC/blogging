from dao.jsonrepo import JsonRepository


class BlogRepository(JsonRepository):
    def fetch_by_owner_id(self, owner_id):
        return [blog for blog in self.find_all() if blog.owner_id == owner_id]
