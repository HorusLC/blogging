from user import User


class Admin(User):

    def __init__(self, f_name, l_name, username, password, salt, gender, email, date_reg, role,cat_moderated,
                 moderation_lvl,id_=None):
        super().__init__(f_name, l_name, username, password, salt, gender, email, date_reg, role, id_)
        self.moderation_lvl = moderation_lvl
        self.cat_moderated = cat_moderated

