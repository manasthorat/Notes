class usermanager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("User does not exist")
        del self.users[username]

    def get_user_email(self, username):
        return self.users.get(username, None)