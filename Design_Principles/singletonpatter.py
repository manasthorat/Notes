class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance
    
    def connect(self):
        if not self.connected:
            self.connected = True
            print("Database connected")
    
    def query(self, sql):
        return f"Executing: {sql}"

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
db1.connect()
print(db2.query("SELECT * FROM users"))