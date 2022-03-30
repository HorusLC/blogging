from entity.user import User


class Blogger(User):

    def __init__(self, f_name, l_name, username, password, salt, gender, email, date_reg, role,
                 blogs_created: list['entity.blog.Blog'],
                 comments_made: list['entity.comment.Comment'], blogs_followed: list['entity.blog.Blog'], last_login,
                 introduction, id_=None):
        super().__init__(f_name, l_name, username, password, salt, gender, email, date_reg, role, id_)
        self.introduction = introduction
        self.last_login = last_login
        self.blogs_followed = blogs_followed
        self.comments_made = comments_made
        self.blogs_created = blogs_created
