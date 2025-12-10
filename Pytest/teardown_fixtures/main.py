class database:
    """simulate a basic user database"""
    def __init__(self):
        self.data = {}
    def add_user(self,user_id,name):
        if user_id in self.data:
            raise ValueError("User already exists")
        self.data[user_id] = name

    def get_user(self,user_id):
        return self.data.get(user_id,None)
    
    def delete_user(self,user_id):
        if user_id not in self.data:
            raise ValueError("User does not exist")
        del self.data[user_id]

    def close(self):
        """Teardown/close the database connection (simulated)."""
        # Clear stored data to simulate closing connection/resources
        self.data.clear()