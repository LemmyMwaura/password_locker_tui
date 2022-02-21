class User:
    number_of_users = 0
    user_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.id = User.number_of_users + 1
        self.credential_list = []
        User.add_user()

    def save_user(self):
        User.user_list.append(self)
    
    def delete_user(self):
        User.user_list.remove(self)
        User.remove_user

    @classmethod
    def add_user(cls):
        cls.number_of_users += 1

    @classmethod
    def remove_user(cls):
        cls.number_of_users -= 1
    
    @classmethod
    def total_number_of_users(cls):
        return cls.number_of_users