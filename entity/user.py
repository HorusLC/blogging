class User:

    def __init__(self, f_name, l_name, username, password, salt, gender, email, date_reg, role,id_=None):
        self.role = role
        self.date_reg = date_reg
        self.email = email
        self.gender = gender
        self.salt = salt
        self.password = password
        self.username = username
        self.l_name = l_name
        self.f_name = f_name
        self.id_ = id_

    def __str__(self):
        return self.f_name + " " + self.l_name

