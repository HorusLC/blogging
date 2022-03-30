from user import User


class Admin(User):

    def __init__(self, id_, f_name, l_name, username, password, salt, gender, email, date_reg, role,cat_moderated,
                 moderation_lvl):
        super().__init__(id_, f_name, l_name, username, password, salt, gender, email, date_reg, role)
        self.moderation_lvl = moderation_lvl
        self.cat_moderated = cat_moderated

