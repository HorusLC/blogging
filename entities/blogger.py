from user import User


class Blogger(User):

    def __init__(self, id_, f_name, l_name, username, password, salt, gender, email, date_reg, role, blogs_created,
                 comments_made, blogs_followed, last_login, introduction):
        super().__init__(id_, f_name, l_name, username, password, salt, gender, email, date_reg, role)
        self.introduction = introduction
        self.last_login = last_login
        self.blogs_followed = blogs_followed
        self.comments_made = comments_made
        self.blogs_created = blogs_created
