class Database:
    """simulate a basic user database"""
    def __init__(self):
        self.data = {}

    def add_user(self, user_id, name):
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = name

    def get_user(self, user_id  ):
        return self.data.get(user_id, None)
    
    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]